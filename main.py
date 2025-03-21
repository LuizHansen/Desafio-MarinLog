from fastapi import FastAPI
import uvicorn
from db import get_db
from config.settings import HOST, PORT, RELOAD
from routes.cnab_router import cnab_router

app = FastAPI()

app.include_router(cnab_router)

get_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=RELOAD)