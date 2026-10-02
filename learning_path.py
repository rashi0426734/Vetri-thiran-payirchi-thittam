from ai_client import get_gemini

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a structured learning path for "{topic}".
Organize it from beginner to intermediate to advanced.
For each level, include key topics, an estimated study time, practice ideas,
and suggested types of learning resources such as tutorials, articles, books, or videos.
Make the plan practical and easy to follow.
"""
    return get_gemini().generate(prompt, max_output_tokens=1800)
