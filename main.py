"""Encapsulate FastAPI interactions."""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Return test message."""
    return {"message": "Hello World"}
