import random
import pandas as pd

def get_home_team_win_chance(home_team: str, away_team: str, season: str, df_stats:pd.DataFrame, models_dict: dict) -> float:
    season_artifacts = models_dict.get(season)
    if not season_artifacts:
        raise ValueError(f"Brak modelu dla sezonu {season}")
    
    model = season_artifacts['model']
    scaler = season_artifacts['scaler']
    features = season_artifacts['features']
    
    stats_season = df_stats[df_stats['SEASON_YEAR'] == season]
    home_stats = stats_season[stats_season['TEAM_ABBREVIATION'] == home_team].iloc[0]
    away_stats = stats_season[stats_season['TEAM_ABBREVIATION'] == away_team].iloc[0]

    delta_plus_minus = home_stats['AVG_PLUS_MINUS'] - away_stats['AVG_PLUS_MINUS']
    delta_win_pct = home_stats['WIN_PCT'] - away_stats['WIN_PCT']
    delta_home_away_win_pct = home_stats['HOME_WIN_PCT'] - away_stats['AWAY_WIN_PCT']

    X_input = pd.DataFrame([[delta_plus_minus, delta_win_pct, delta_home_away_win_pct]], columns=features)
    X_scaled = scaler.transform(X_input)
    prob = model.predict_proba(X_scaled)
    
    home_team_win_chance = prob[0][1]
    
    return home_team_win_chance

def simulate_single_match(home_team_win_chance: float) -> bool:
    return random.random() < home_team_win_chance


def simulate_single_series(home_team, away_team, season):
    
    home_team_score = 0
    away_team_score = 0
    
    home_team_win_chance = get_home_team_win_chance(home_team, away_team, season)
    
    while True:
        if simulate_single_match(home_team_win_chance):
            home_team_score+=1
        else:
            away_team_score+=1
            
        if home_team_score == 4:
            return home_team
        elif away_team_score == 4:
            return away_team