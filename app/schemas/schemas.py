from pydantic import BaseModel


class SummarizerQuery(BaseModel):
    text: str


class SummarizerResponse(BaseModel):
    summary: str


class SaarGenQuery(BaseModel):
    description: str