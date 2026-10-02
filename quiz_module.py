import json
import re
from ai_client import get_gemini

def _clean_json(text: str) -> str:
    text = re.sub(r"```(?:json)?", "", text, flags=re.I)
    return text.replace("```", "").strip()

def generate_quiz(text: str) -> list:
    prompt = f"""
You are a quiz generator for EduGenie.
From the passage below, create exactly 3 multiple-choice questions.
Each question must contain exactly 4 options and one correct answer.
Return ONLY valid JSON in this format:
[
  {{"question":"...", "options":["...","...","...","..."], "answer":"..."}}
]

PASSAGE:
{text}
"""
    raw = get_gemini().generate(prompt, max_output_tokens=1200)
    data = json.loads(_clean_json(raw))
    if not isinstance(data, list) or len(data) != 3:
        raise ValueError("Gemini did not return exactly 3 quiz questions")
    for item in data:
        if not all(k in item for k in ("question", "options", "answer")):
            raise ValueError("Invalid quiz item")
        if len(item["options"]) != 4:
            raise ValueError("Each quiz question must have 4 options")
    return data
