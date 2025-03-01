from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router import router as router_crypto

app = FastAPI()

app.include_router(router_crypto)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем только с этого URL
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST, и т.д.)
    allow_headers=["*"],  # Разрешаем все заголовки
)

