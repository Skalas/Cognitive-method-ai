from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas, models


router = APIRouter()


@router.get("/", summary="Welcome Message", description="Returns a welcome message.")
def read_root():
    return {"message": "Welcome to Metodo Cognitivo!"}
