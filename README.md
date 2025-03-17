# SaarGen-Summarizer

A simple app for AI summary generation

###  Directory Structure
```zsh
 app
    ├── core
    │   ├── inference.py
    │   └── __init__.py
    ├── docker-compose.yaml
    ├── Dockerfile
    ├── __init__.py
    ├── main.py
    ├── requirements.txt
    ├── schemas
    │   ├── __init__.py
    │   └── schemas.py
    └── tests
        ├── __init__.py
        └── test_main.py
```

## Getting Started
1. Install dependencies
* [Docker](https://docs.docker.com/engine/install/)
* [docker-compose](https://docs.docker.com/compose/install/)

2. Clone the repository
```zsh
git clone https://github.com/kakadeniranjan1999/SaarGen-Summarizer.git
cd SaarGen-Summarizer/app
```

3. Edit .env file
* `HF_API_KEY` Huggingface API key for Inference API
* `INFERENCE_PROVIDER` Inference provider on for Huggingface's serverless Inference API (default=`hf-inference`)
* `MODEL_NAME` Summarization model name for Huggingface Hub (default=`google/pegasus-xsum`)
* `PORT` Port number for application. Update the same in [docker-compose.yaml](app/docker-compose.yaml) (default=`5001`)

4. Build and run docker container
```zsh
docker compose up --build
```

5. Stop docker container
```zsh
docker compose stop
```

## Testing
```zsh
python -m pytest test/test_main.py
```

## API Documentation

Detailed documentation of SaarGen Summarizer ca be accessed at [http://0.0.0.0:5001/docs](http://0.0.0.0:5001/docs). The code snippet for each API is described below.

### 1. Query Description - Responds with a simple acknowledgement (SaarGen's description).

### Request

`GET /query/`

```zsh
import requests

url = "http://0.0.0.0:5001/query"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

### Response

    {
    "description": "Hello! I am SaarGen! Your AI summary generator. My name is a combination of Sanskrit word Saaransh (meaning Summary in English) and Generator!"
    }

### 2. Summarize Text - Receives text input and returns summarized content generated using an AI model.

### Request

`POST /summarize/`

```zsh
import requests
import json

url = "http://0.0.0.0:5001/summarize"

payload = json.dumps({
  "text": "The Inflation Reduction Act lowers prescription drug costs, health care costs, and energy costs. It's the most aggressive action on tackling the climate crisis in American history which will lift up American workers and create good-paying, union jobs across the country. It'll lower the deficit and ask the ultra-wealthy and corporations to pay their fair share. And no one making under $400,000 per year will pay a penny more in taxes."
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

### Response

    {
    "summary": "President Obama has signed into law one of the biggest tax cuts in history."
    }

## Scope for Improvement

```Due to the issues faced while sending kwargs to Inference API, handling summarization length is not implemented.```

## Contact

```Niranjan Kakade - niranjankakade06@gmail.com```
