from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import (
    QARequest, ExplainRequest, QuizRequest, SummaryRequest,
    LearningPathRequest, QAResponse, ExplainResponse,
    QuizResponse, SummaryResponse, LearningPathResponse
)
from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie", version="1.0.0")
BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}


@app.post("/qa", response_model=QAResponse)
async def qa(payload: QARequest):
    try:
        return QAResponse(answer=answer_question(payload.question))
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"AI service error: {exc}")


@app.post("/explain", response_model=ExplainResponse)
async def explain(payload: ExplainRequest):
    try:
        return ExplainResponse(topic=payload.topic, explanation=explain_topic(payload.topic))
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"AI service error: {exc}")


@app.post("/quiz", response_model=QuizResponse)
async def quiz(payload: QuizRequest):
    try:
        return QuizResponse(quiz=generate_quiz(payload.text))
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"AI service error: {exc}")


@app.post("/summarize", response_model=SummaryResponse)
async def summarize(payload: SummaryRequest):
    try:
        return SummaryResponse(summary=summarize_text(payload.text))
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"AI service error: {exc}")


@app.post("/learn/recommendations", response_model=LearningPathResponse)
async def learning_path(payload: LearningPathRequest):
    try:
        return LearningPathResponse(
            topic=payload.topic,
            recommendation=get_learning_recommendations(payload.topic)
        )
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"AI service error: {exc}")
