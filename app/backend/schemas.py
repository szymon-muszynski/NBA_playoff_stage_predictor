from pydantic import BaseModel

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