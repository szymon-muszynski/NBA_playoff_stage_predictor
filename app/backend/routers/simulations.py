from fastapi import APIRouter, Request, HTTPException

from schemas import SeriesSimulationRequest, SeriesSimulationResponse
from simulation import simulate_single_series

router = APIRouter(prefix="/api/simulations", tags=["Symulacje NBA"])

@router.get("/api/message")
def get_message():
    return {"message": "Cześć! Tu backend w FastAPI!"}

# Główny endpoint do symulacji pojedynczej serii
@router.post("/api/simulate_series", response_model=SeriesSimulationResponse)
def simulate_series(payload: SeriesSimulationRequest, request: Request):
    """
    Endpoint przyjmuje JSONa w formacie SeriesSimulationRequest, 
    wyciąga modele z RAMu i deleguje obliczenia do simulation.py.
    """
    
    # Wyciągamy załadowane przy starcie dane z app.state
    df_stats = request.app.state.df_stats
    models_dict = request.app.state.models_dict
    
    try:
        # Odpalamy Twoją funkcję!
        winner = simulate_single_series(
            home_team=payload.home_team,
            away_team=payload.away_team,
            season=payload.season,
            df_stats=df_stats,
            models_dict=models_dict
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