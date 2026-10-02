from functools import lru_cache
from google import genai
from google.genai import types
from config import settings

class GeminiService:
    def __init__(self):
        if not settings.gemini_api_key:
            raise RuntimeError("GEMINI_API_KEY is not configured in .env")
        self.client = genai.Client(api_key=settings.gemini_api_key)
        self.model = settings.gemini_model

    def generate(self, prompt: str, max_output_tokens: int = 1200) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                 max_output_tokens=2000,
    response_mime_type="application/json"
            ),
        )
        text = getattr(response, "text", None)
        if not text:
            raise RuntimeError("Gemini returned an empty response")
        return text.strip()

@lru_cache
def get_gemini():
    return GeminiService()
