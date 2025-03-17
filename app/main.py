import logging
import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from requests.exceptions import ConnectionError, ReadTimeout
from huggingface_hub.errors import HTTPError, InferenceTimeoutError
from fastapi.exceptions import ResponseValidationError, RequestValidationError

from schemas.schemas import SummarizerQuery, SummarizerResponse, SaarGenQuery
from core.inference import SaarGenSummarizer
from core.logger import get_logger


logger = get_logger(uvicorn.config.logger)

load_dotenv()
PORT = int(os.getenv("PORT"))


app = FastAPI(
    title="SaarGen Summarizer",
    version="1.0",
    summary="A simple app for AI summary generation"
)

saar_gen = SaarGenSummarizer()


@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request, error):
    logger.error(f"ResponseValidationError ---> {request} ---> {error}")
    raise HTTPException(status_code=500, detail=f"Internal Server Error!!!")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, error):
    logger.error(f"RequestValidationError ---> {request} ---> {error}")
    raise HTTPException(status_code=400, detail=f"{error.__class__.__name__}: {error.__str__()}")

@app.get("/query", response_model=SaarGenQuery, response_description="SaarGen's Description")
async def query_description():
    """
    Responds with a simple acknowledgement (SaarGen's description).
    """
    logger.info(f"API call ---> /query/")
    return {
        "description": "Hello! I am SaarGen! Your AI summary generator. My name is a combination of Sanskrit word "
                       "Saaransh (meaning Summary in English) and Generator!",
    }

@app.post("/summarize/", response_model=SummarizerResponse, response_description="The generated summary.")
async def summarize_text(text: SummarizerQuery):
    """
    Receives text input and returns summarized content generated using an AI model.
    - **text**: Long text to use for summary generation.
    """
    logger.info(f"API call ---> /summarize/ ---> {text.text}")
    try:
        summary = saar_gen.generate_summary(text.text)
        response = {
            "summary": summary.strip(),
        }
        logger.info(f"API call success ---> /summarize/ ---> {response['summary']}")
    except ConnectionError as error:
        logger.error(f"ConnectionError ---> {error}")
        raise HTTPException(status_code=400, detail="Connection Error!!!")
    except ReadTimeout as error:
        logger.error(f"ReadTimeout ---> {error}")
        raise HTTPException(status_code=408, detail=f"{error.__class__.__name__}: {error.__str__()}")
    except InferenceTimeoutError as error:
        logger.error(f"InferenceTimeoutError ---> {error}")
        raise HTTPException(status_code=504, detail=f"{error.__class__.__name__}: {error.__str__()}")
    except HTTPError as error:
        logger.error(f"HTTPError ---> {error}")
        raise HTTPException(status_code=400, detail=f"{error.__class__.__name__}: {error.__str__()}")
    except Exception as error:
        logger.error(f"General Exception ---> {error}")
        raise HTTPException(status_code=500, detail="Something Went Wrong!!!")

    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=PORT, reload=True, use_colors=True)
