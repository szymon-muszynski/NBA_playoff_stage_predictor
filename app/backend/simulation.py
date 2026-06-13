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


def simulate_single_series(home_team: str, away_team: str, season: str, df_stats:pd.DataFrame, models_dict: dict) -> str:
    
    home_team_score = 0
    away_team_score = 0
    game_number = 1
    
    while True:
        
        if game_number in [1,2,5,7]:
            current_host = home_team
            current_guest = away_team
        else:
            current_host = away_team
            current_guest = home_team
        
        host_team_win_chance = get_home_team_win_chance(current_host, current_guest, season, df_stats, models_dict)
        
        current_host_win = simulate_single_match(host_team_win_chance)
        
        if current_host_win:
            if current_host == home_team:
                home_team_score += 1
            else:
                away_team_score += 1
        else:
            if current_guest == home_team:
                home_team_score += 1
            else:
                away_team_score += 1
                
        print(f"Gra {game_number}: {home_team} - {home_team_score}:{away_team_score} {away_team}")        
        
        if home_team_score == 4:
            return home_team
        elif away_team_score == 4:
            return away_team
        
        game_number += 1