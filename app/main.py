from fastapi import FastAPI
from app.routers import training_generation
from contextlib import asynccontextmanager
from app.rag import initialize_ai


app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    print("Starting up...")
    # await database.connect()
    initialize_ai()
    yield
    # Shutdown event
    print("Shutting down...")
    # await database.disconnect()


app.router.lifespan_context = lifespan
app.include_router(training_generation.router, prefix="/v1")
