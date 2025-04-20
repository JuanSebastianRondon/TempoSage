# save this as app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Buenas!"

