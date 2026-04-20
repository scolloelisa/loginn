from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import pandas as pd

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/") # Endpoint: punto in cui andiamo a richiamare il server web
def home():
    # Restituisce direttamente il file HTML
    return FileResponse('static/index.html')

@app.get("/login")
def Controlla(username: str, password: str):
    print("username ", username, "password ", password)
    if username.lower() == "admin" and password == "xxx123":
        return RedirectResponse(url="/static/pagina.html")
    else:
        risposta = {"messaggio": "accesso negato"}
        return (risposta)
    