from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from db import cria_tabelas
from config.settings import HOST, PORT, RELOAD
from routes.cnab_router import cnab_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cnab_router)


cria_tabelas()

if __name__ == "__main__":
    uvicorn.run("server.main:app", host=HOST, port=int(PORT), reload=RELOAD)