from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


@router.get(
    "/exercises?tipo_de_ejercicio={tipo_de_ejercicio}&edades={edades}&cantidad_de_jugadores={cantidad_de_jugadores}",
    response_model= ...,
    summary="Get exercises filtered by type, age group, and number of players",
    description="Retrieve a list of exercises based on the provided type, age group, and number of players.",
)
async def get_exercises(
    tipo_de_ejercicio: str,
    edades: str,
    cantidad_de_jugadores: str,
):
    ...


@router.get(
    "/exercises?cantidad_de_jugadores={cantidad_de_jugadores}",
    response_model= ...,
    summary="Get exercises filtered by number of players",
    description="Retrieve a list of exercises suitable for a given number of players.",
)
async def get_exercises_by_players(
    cantidad_de_jugadores: str,
):
    ...


@router.get(
    "/exercises?tipo_de_ejercicio={tipo_de_ejercicio}&edades={edades}",
    response_model= ...,
    summary="Get exercises filtered by type and age group",
    description="Retrieve a list of exercises based on the type and age group.",
)
async def get_exercises_by_type_and_age(
    tipo_de_ejercicio: str,
    edades: str,
    
):
    ...


@router.get(
    "/exercises?tipo_de_ejercicio={tipo_de_ejercicio}",
    response_model= ...,
    summary="Get exercises filtered by type",
    description="Retrieve a list of exercises based on the exercise type.",
)
async def get_exercises_by_type(
    tipo_de_ejercicio: str,
    
):
    ...


@router.get(
    "/exercises?edades={edades}",
    response_model= ...,
    summary="Get exercises filtered by age group",
    description="Retrieve a list of exercises suitable for a specific age group.",
)
async def get_exercises_by_age(
    edades: str,
    
):
    ...


@router.get(
    "/exercises?tipo_de_ejercicio={tipo_de_ejercicio}&cantidad_de_jugadores={cantidad_de_jugadores}",
    response_model= ...,
    summary="Get exercises filtered by type and number of players",
    description="Retrieve a list of exercises based on the type and number of players.",
)
async def get_exercises_by_type_and_age(
    tipo_de_ejercicio: str,
    edades: str,
    
):
    ...