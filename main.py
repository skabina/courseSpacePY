from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/files/{file_path}")
def read_file(file_path: str):
    return {"file_path": file_path}