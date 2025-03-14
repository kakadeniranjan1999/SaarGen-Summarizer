from huggingface_hub import AsyncInferenceClient, InferenceClient
import os


HF_API_KEY = os.getenv("HF_API_KEY")
INFERENCE_PROVIDER = os.getenv("INFERENCE_PROVIDER")
MODEL_NAME = os.getenv("MODEL_NAME")

class SaarGenSummarizer:
    def __init__(self):
        self.client = InferenceClient(
            provider=INFERENCE_PROVIDER,
            api_key=HF_API_KEY,
            timeout=10.0
        )

    def generate_summary(self, text):
        result = self.client.summarization(
            text=text,
            model=MODEL_NAME,
        )
        return result.summary_text
