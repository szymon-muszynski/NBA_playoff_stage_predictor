from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import pandas as pd
import joblib
from pathlib import Path
from routers import simulations

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

STATS_PATH = "regular_season_stats_from_2010-11_to_2023-24.csv"
MODELS_PATH = "models_by_season.joblib"

# 1. Mechanizm Lifespan - Zarządzanie cyklem życia serwera
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("⏳ Ładowanie statystyk i modeli do pamięci RAM...")
    app.state.df_stats = pd.read_csv(DATA_DIR / STATS_PATH)
    app.state.models_dict = joblib.load(DATA_DIR / MODELS_PATH)
    print("✅ Serwer gotowy do symulacji!")
    
    yield 
    
    print("🔴 Zamykanie serwera, zwalnianie pamięci...")
    app.state.models_dict.clear()

# Przypisujemy lifespan do naszej aplikacji
app = FastAPI(lifespan=lifespan)

app.include_router(simulations.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)