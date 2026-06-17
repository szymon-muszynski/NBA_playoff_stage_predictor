from fastapi import APIRouter, Request, HTTPException, Depends

from schemas import SeriesSimulationRequest, SeriesSimulationResponse, PlayoffSimulationResponse, PlayoffSimulationRequest
from simulation import simulate_single_series, simulate_whole_playoffs



router = APIRouter(prefix="/api/simulations", tags=["Symulacje NBA"])

@router.get("/api/message")
def get_message():
    return {"message": "Cześć! Tu backend w FastAPI!"}


def get_ml_models(request: Request):
     return request.app.state.models_dict

def get_stats(request: Request):
    return request.app.state.df_stats

def get_matchups(request: Request):
    return request.app.state.matchups

# Główny endpoint do symulacji pojedynczej serii
@router.post("/series", response_model=SeriesSimulationResponse)
def simulate_series(payload: SeriesSimulationRequest, prediction_models = Depends(get_ml_models), season_stats = Depends(get_stats)):
    """
    Endpoint przyjmuje JSONa w formacie SeriesSimulationRequest, 
    wyciąga modele z RAMu i deleguje obliczenia do simulation.py.
    """
    
    try:
        winner, _ = simulate_single_series(
            home_team=payload.home_team,
            away_team=payload.away_team,
            season=payload.season,
            df_stats=season_stats,
            models_dict=prediction_models
        )
        
    
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
    
    
@router.post('/whole_playoffs', response_model=PlayoffSimulationResponse)
def whole_playoffs_simulation(
        payload: PlayoffSimulationRequest,
        prediction_models = Depends(get_ml_models),
        season_stats = Depends(get_stats),
        playoff_matchups = Depends(get_matchups)
    ):
    
    try:
        result = simulate_whole_playoffs(
            matchups=playoff_matchups,
            season=payload.season,
            df_stats=season_stats,
            models_dict=prediction_models
        )
    
        return result
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except KeyError:
        raise HTTPException(status_code=400, detail="Brak danych dla podanego sezonu lub błąd w drabince.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Błąd symulacji: {str(e)}")