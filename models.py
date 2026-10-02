from pydantic import BaseModel, Field
from typing import List

class QARequest(BaseModel):
    question: str = Field(min_length=1)

class ExplainRequest(BaseModel):
    topic: str = Field(min_length=1)

class QuizRequest(BaseModel):
    text: str = Field(min_length=1)

class SummaryRequest(BaseModel):
    text: str = Field(min_length=1)

class LearningPathRequest(BaseModel):
    topic: str = Field(min_length=1)

class QAResponse(BaseModel):
    answer: str

class ExplainResponse(BaseModel):
    topic: str
    explanation: str

class QuizItem(BaseModel):
    question: str
    options: List[str]
    answer: str

class QuizResponse(BaseModel):
    quiz: List[QuizItem]

class SummaryResponse(BaseModel):
    summary: str

class LearningPathResponse(BaseModel):
    topic: str
    recommendation: str
