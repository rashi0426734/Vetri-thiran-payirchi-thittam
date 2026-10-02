from ai_client import get_gemini

def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational passage in simple language.
Keep the important facts and ideas, remove repetition, and use short paragraphs or bullets when helpful.

PASSAGE:
{text}
"""
    return get_gemini().generate(prompt, max_output_tokens=1000)
