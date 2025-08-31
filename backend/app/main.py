from fastapi import FastAPI
from .routers import data, auth

from backend.app.routers import data

app = FastAPI(title="Energy Backend API")

app.include_router(data.router, prefix="/api")
app.include_router(auth.router)



@app.get("/hello")
async def hello():
    return {"message": "Hello from FastAPI backend!"}
