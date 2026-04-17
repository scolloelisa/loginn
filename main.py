from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/") # Endpoint: punto in cui andiamo a chiamare il server web
def home():
    # Restituisce direttamente il file HTML
    return FileResponse('static/index.html')

@app.get("/login")
def Login():
    return