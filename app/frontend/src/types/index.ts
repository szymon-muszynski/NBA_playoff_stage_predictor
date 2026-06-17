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

export interface PlayoffSimulationRequest {
  season: string;
}

export interface SingleSeriesResult {
  team_a: string;
  team_b: string;
  winner: string;
  winners_history: string[];
}

export interface PlayoffsRoundsResults {
  round_1: SingleSeriesResult[];
  round_2: SingleSeriesResult[];
  conference_finals: SingleSeriesResult[];
}

export interface Bracket {
  Eastern: PlayoffsRoundsResults;
  Western: PlayoffsRoundsResults;
}

export interface PlayoffSimulationResponse {
  season: string;
  champion: string;
  bracket: Bracket;
  nba_finals: SingleSeriesResult;
}