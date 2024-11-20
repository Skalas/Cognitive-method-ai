from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas, models
from app.vertex_ai import generate_text_with_gemini

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
    a = generate_text_with_gemini(training_request.question)
    return {"response": a}
