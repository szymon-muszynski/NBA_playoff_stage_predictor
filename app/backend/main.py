from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Konfiguracja CORS - dzięki temu frontend (np. na porcie 5173) 
# może wysyłać zapytania do backendu (na porcie 8000).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # W produkcji zmieniasz na adres swojego frontendu!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prosty testowy endpoint
@app.get("/api/message")
def get_message():
    return {"message": "Cześć! Tu backend w FastAPI!"}