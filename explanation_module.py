from ai_client import get_gemini

def explain_topic(topic: str) -> str:
    prompt = f"""
Explain the concept "{topic}" in a simple, clear way for a school or college student.
Start with a short definition, then explain the key idea using a simple example.
Avoid unnecessary jargon.
"""
    return get_gemini().generate(prompt)
