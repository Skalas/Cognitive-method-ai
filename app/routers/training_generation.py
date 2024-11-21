from fastapi import APIRouter, Depends, HTTPException
from app import schemas
from app.vertex_ai import generate_text_with_gemini
from app.rag import get_parameters_gemini, get_exercises_rag_gemini
import json

router = APIRouter()


@router.get("/", summary="Welcome Message", description="Returns a welcome message.")
def read_root():
    return {"message": "Welcome to Metodo Cognitivo!"}


@router.post(
    "/generate-training",
    summary="Generate Training configuration",
    description="Generate training configuration for the coach.",
)
async def generate_training_configuration(
    training_request: schemas.TrainingRequest,
):
    params = get_parameters_gemini(training_request.question)
    exercises = get_exercises_rag_gemini(params)
    json_response = json.loads(exercises.replace("```json", "").replace("```", ""))

    return json_response
