from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseSettings

    #   BACK_PORT: ${BACK_PORT}
    #   FRONT_PORT: ${FRONT_PORT}
    #   NGINX_PORT: ${NGINX_PORT}
    #   POSTGRES_HOST: ${POSTGRES_HOST}
    #   POSTGRES_DB: ${POSTGRES_DB}
    #   POSTGRES_USER: ${POSTGRES_USER}
    #   POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    #   POSTGRES_PORT: ${POSTGRES_PORT}

class Settings(BaseSettings):
    BACK_PORT: str
    FRONT_PORT: str
    NGINX_PORT: str
    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: str

settings = Settings()

app = FastAPI()

origins = [
    # f"http://localhost:{settings.BACK_PORT}",
    f"https://localhost:{settings.FRONT_PORT}",
    f"https://localhost:{settings.NGINX_PORT}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # allow_methods=["GET,HEAD,PUT,PATCH,POST,DELETE,OPTIONS"],
    # allow_headers=["Content-Type", "API-Key", "Authentication"],
)

@app.post("/api")
async def read_root():
    return {"Hello": "World"}