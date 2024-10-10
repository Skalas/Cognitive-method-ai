from fastapi import FastAPI

from app import database
from app import models
from app.routers import appointment_report
from app.vertex_ai import initialize_vertex_ai
from contextlib import asynccontextmanager

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    print("Starting up...")
    # await database.connect()
    initialize_vertex_ai()
    yield
    # Shutdown event
    print("Shutting down...")
    # await database.disconnect()


app.router.lifespan_context = lifespan


app.include_router(appointment_report.router, prefix="/v1")
