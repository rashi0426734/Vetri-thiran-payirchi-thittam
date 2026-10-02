from ai_client import get_gemini

def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant.
Answer the student's question accurately and concisely.
Use clear language suitable for a learner.
Question: {question}
"""
    return get_gemini().generate(prompt)
