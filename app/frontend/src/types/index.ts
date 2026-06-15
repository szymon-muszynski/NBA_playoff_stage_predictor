export interface SeriesSimulationRequest {
  season: string;
  home_team: string;
  away_team: string;
}

export interface SeriesSimulationResponse {
  season: string;
  matchup: string;
  winner: string;
}