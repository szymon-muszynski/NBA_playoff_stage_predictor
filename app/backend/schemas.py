from pydantic import BaseModel
from typing import List

# Definiujemy, czego oczekujemy od frontendu
class SeriesSimulationRequest(BaseModel):
    season: str
    home_team: str  # Drużyna wyżej rozstawiona
    away_team: str  # Drużyna niżej rozstawiona

# Definiujemy, co obiecuje zwrócić backend
class SeriesSimulationResponse(BaseModel):
    season: str
    matchup: str
    winner: str
    
class PlayoffSimulationRequest(BaseModel):
    season: str

class SingleSeriesResult(BaseModel):
    team_a: str
    team_b: str
    winner: str
    winners_history: List[str]
    
class PlayoffsRoundsResults(BaseModel):
    round_1: List[SingleSeriesResult]
    round_2: List[SingleSeriesResult]
    conference_finals: List[SingleSeriesResult]
    
class Bracket(BaseModel):
    Eastern: PlayoffsRoundsResults
    Western: PlayoffsRoundsResults

class PlayoffSimulationResponse(BaseModel):
    season: str
    champion: str
    bracket: Bracket
    nba_finals: SingleSeriesResult
    