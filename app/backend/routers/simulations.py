from fastapi import APIRouter, Request, HTTPException, Depends

from schemas import SeriesSimulationRequest, SeriesSimulationResponse
from simulation import simulate_single_series

router = APIRouter(prefix="/api/simulations", tags=["Symulacje NBA"])

@router.get("/api/message")
def get_message():
    return {"message": "Cześć! Tu backend w FastAPI!"}

#Tworzysz funkcję "Dostawcę", która wyciąga to, co trzeba z Requesta
def get_ml_models(request: Request):
     return request.app.state.models_dict

def get_stats(request: Request):
    return request.app.state.df_stats

# Główny endpoint do symulacji pojedynczej serii
@router.post("/api/simulate_series", response_model=SeriesSimulationResponse)
def simulate_series(payload: SeriesSimulationRequest, prediction_models = Depends(get_ml_models), season_stats = Depends(get_stats)):
    """
    Endpoint przyjmuje JSONa w formacie SeriesSimulationRequest, 
    wyciąga modele z RAMu i deleguje obliczenia do simulation.py.
    """
    
    try:
        # Odpalamy Twoją funkcję!
        winner = simulate_single_series(
            home_team=payload.home_team,
            away_team=payload.away_team,
            season=payload.season,
            df_stats=season_stats,
            models_dict=prediction_models
        )
        
        # Formujemy i zwracamy odpowiedź zgodną z naszym schematem
        return SeriesSimulationResponse(
            season=payload.season,
            matchup=f"{payload.home_team} vs {payload.away_team}",
            winner=winner
        )
        
    except ValueError as e:
        # Jeśli np. nie ma modelu dla danego sezonu
        raise HTTPException(status_code=404, detail=str(e))
    except IndexError:
        # Jeśli drużyna nie istnieje w danym sezonie
        raise HTTPException(status_code=400, detail="Nie znaleziono podanej drużyny w tym sezonie.")