from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración del middleware CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servicio raíz
@app.get("/", response_class=PlainTextResponse)
def raiz():
    return "RAIZ – API, método GET"

# Servicio /hello/
@app.get("/hello/", response_class=PlainTextResponse)
def hello():
    return "Esta es la API inicial de ITI-621 IIIC-2025"

# Servicio /api/personas
@app.get("/api/personas")
def obtener_persona():
    persona = {
        "id": 1,
        "nombre": "Johana",
        "telefono": "64336733"
    }
    return persona