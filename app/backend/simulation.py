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


def simulate_single_series(home_team: str, away_team: str, season: str, df_stats:pd.DataFrame, models_dict: dict) -> tuple:
    
    home_team_score = 0
    away_team_score = 0
    game_number = 1
    
    history = []
    
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
                history.append(home_team)
            else:
                away_team_score += 1
                history.append(away_team)
        else:
            if current_guest == home_team:
                home_team_score += 1
                history.append(home_team)
            else:
                away_team_score += 1
                history.append(away_team)
                
        #print(f"Gra {game_number}: {home_team} - {home_team_score}:{away_team_score} {away_team}")        
        
        if home_team_score == 4:
            return home_team, history
        elif away_team_score == 4:
            return away_team, history
        
        game_number += 1
        
def simulate_whole_playoffs(matchups: dict, season: str,  df_stats:pd.DataFrame, models_dict: dict) -> dict:
    result = {
        "season": season,
        "champion": "",
        "bracket": {
            "Eastern": {},
            "Western": {}
        },
        "nba_finals": {}
    }
    
    winner_1_8_east = {}
    winner_2_7_east = {}
    winner_3_6_east = {}
    winner_4_5_east = {}
    
    winner_1_8_west = {}
    winner_2_7_west = {}
    winner_3_6_west = {}
    winner_4_5_west = {}
    
    season_matchups_eastern = matchups[season]["Eastern"]
    season_matchups_western = matchups[season]["Western"]
    
    round_1_eastern_series = []
    
    for match in season_matchups_eastern:
        if match['seed_a'] < match['seed_b']:
            home_team = match['team_a']
            away_team = match['team_b']
        else:
            home_team = match['team_b']
            away_team = match['team_a']
            
        winner, history = simulate_single_series(home_team, away_team, season, df_stats, models_dict)
        
        if winner == match['team_a']:
            winner_seed = match['seed_a']
        else:
            winner_seed = match['seed_b']
        
        winner_data = {
            "team_name": winner,
            "seed": winner_seed
        }
        
        series_recap = {}
        
        series_recap["team_a"] = match["team_a"]
        series_recap["team_b"] = match["team_b"]
        series_recap["winner"] = winner
        series_recap["winners_history"] = history
        
        round_1_eastern_series.append(series_recap)
        
        if match['seed_a'] == 1:
            winner_1_8_east = winner_data
        elif match['seed_a'] == 2:
            winner_2_7_east = winner_data
        elif match['seed_a'] == 3:
            winner_3_6_east = winner_data
        else:
            winner_4_5_east = winner_data
    
    result["bracket"]["Eastern"]["round_1"] = round_1_eastern_series
    
    round_1_western_series = []
    
    for match in season_matchups_western:
        if match['seed_a'] < match['seed_b']:
            home_team = match['team_a']
            away_team = match['team_b']
        else:
            home_team = match['team_b']
            away_team = match['team_a']
            
        winner, history = simulate_single_series(home_team, away_team, season, df_stats, models_dict)
        
        if winner == match['team_a']:
            winner_seed = match['seed_a']
        else:
            winner_seed = match['seed_b']
        
        winner_data = {
            "team_name": winner,
            "seed": winner_seed
        }
        
        series_recap = {}
        
        series_recap["team_a"] = match["team_a"]
        series_recap["team_b"] = match["team_b"]
        series_recap["winner"] = winner
        series_recap["winners_history"] = history
        
        round_1_western_series.append(series_recap)
        
        if match['seed_a'] == 1:
            winner_1_8_west = winner_data
        elif match['seed_a'] == 2:
            winner_2_7_west = winner_data
        elif match['seed_a'] == 3:
            winner_3_6_west = winner_data
        else:
            winner_4_5_west = winner_data
            
    result["bracket"]["Western"]["round_1"] = round_1_western_series
    
    conference_semifinal_1_eastern = [winner_1_8_east, winner_4_5_east]
    conference_semifinal_2_eastern = [winner_2_7_east, winner_3_6_east]
    conference_semifinal_1_western = [winner_1_8_west, winner_4_5_west]
    conference_semifinal_2_western = [winner_2_7_west, winner_3_6_west]
    
    conference_semifinals_eastern = [
        conference_semifinal_1_eastern,
        conference_semifinal_2_eastern
    ]
    
    conference_semifinals_western = [
        conference_semifinal_1_western,
        conference_semifinal_2_western
    ]
    
    
    round_2_eastern_series = []
    eastern_conference_finalists = []
    
    for semifinal in conference_semifinals_eastern:
        if semifinal[0]["seed"] < semifinal[1]["seed"]:
            home_team_dict = semifinal[0]
            away_team_dict = semifinal[1]
        else:
            home_team_dict = semifinal[1]
            away_team_dict = semifinal[0]
        
        home_team = home_team_dict["team_name"]
        away_team = away_team_dict["team_name"]
        
        winner, history = simulate_single_series(home_team, away_team, season, df_stats, models_dict)
        
        winner_seed = home_team_dict["seed"] if winner == home_team else away_team_dict["seed"]
        winner_data = {
            "team_name": winner, 
            "seed": winner_seed
            }
        eastern_conference_finalists.append(winner_data)
        
        series_recap = {
            "team_a": home_team,
            "team_b": away_team,
            "winner": winner,
            "winners_history": history
        }
        round_2_eastern_series.append(series_recap)
        
    result["bracket"]["Eastern"]["round_2"] = round_2_eastern_series
    
    round_2_western_series = []
    western_conference_finalists = []
      
    for semifinal in conference_semifinals_western:
        if semifinal[0]["seed"] < semifinal[1]["seed"]:
            home_team_dict = semifinal[0]
            away_team_dict = semifinal[1]
        else:
            home_team_dict = semifinal[1]
            away_team_dict = semifinal[0]
        
        home_team = home_team_dict["team_name"]
        away_team = away_team_dict["team_name"]
        
        winner, history = simulate_single_series(home_team, away_team, season, df_stats, models_dict)
        
        winner_seed = home_team_dict["seed"] if winner == home_team else away_team_dict["seed"]
        winner_data = {
            "team_name": winner, 
            "seed": winner_seed
            }
        
        western_conference_finalists.append(winner_data)
        
        series_recap = {
            "team_a": home_team,
            "team_b": away_team,
            "winner": winner,
            "winners_history": history
        }
        round_2_western_series.append(series_recap)
        
    result["bracket"]["Western"]["round_2"] = round_2_western_series    
    
    # FINAŁY KONFERENCJI
    # wschód
    if eastern_conference_finalists[0]["seed"] < eastern_conference_finalists[1]["seed"]:
        home_team_dict, away_team_dict = eastern_conference_finalists[0], eastern_conference_finalists[1]
    else:
        home_team_dict, away_team_dict = eastern_conference_finalists[1], eastern_conference_finalists[0]
        
    home_team_east = home_team_dict["team_name"]
    away_team_east = away_team_dict["team_name"]
    winner_east, history_east = simulate_single_series(home_team_east, away_team_east, season, df_stats, models_dict)
    
    result["bracket"]["Eastern"]["conference_finals"] = [{
        "team_a": home_team_east,
        "team_b": away_team_east,
        "winner": winner_east,
        "winners_history": history_east
    }]
    
    #zachód
    if western_conference_finalists[0]["seed"] < western_conference_finalists[1]["seed"]:
        home_team_dict, away_team_dict = western_conference_finalists[0], western_conference_finalists[1]
    else:
        home_team_dict, away_team_dict = western_conference_finalists[1], western_conference_finalists[0]
        
    home_team_west = home_team_dict["team_name"]
    away_team_west = away_team_dict["team_name"]
    winner_west, history_west = simulate_single_series(home_team_west, away_team_west, season, df_stats, models_dict)
    
    result["bracket"]["Western"]["conference_finals"] = [{
        "team_a": home_team_west,
        "team_b": away_team_west,
        "winner": winner_west,
        "winners_history": history_west
    }]
    
    #FINAŁ NBA
    
    stats_season = df_stats[df_stats['SEASON_YEAR'] == season]
    east_win_pct = stats_season[stats_season['TEAM_ABBREVIATION'] == winner_east].iloc[0]['WIN_PCT']
    west_win_pct = stats_season[stats_season['TEAM_ABBREVIATION'] == winner_west].iloc[0]['WIN_PCT']
    
    # Drużyna z lepszym bilansem z sezonu regularnego staje się gospodarzem
    if east_win_pct >= west_win_pct:
        nba_home_team = winner_east
        nba_away_team = winner_west
    else:
        nba_home_team = winner_west
        nba_away_team = winner_east

    nba_champion, nba_history = simulate_single_series(nba_home_team, nba_away_team, season, df_stats, models_dict)
    
    result["nba_finals"] = {
        "team_a": nba_home_team,
        "team_b": nba_away_team,
        "winner": nba_champion,
        "winners_history": nba_history
    }
    
    result["champion"] = nba_champion
    
    return result

import pandas as pd
import joblib
import json
from pathlib import Path

# # 1. Ten krok automatycznie namierzy folder 'backend' na Twoim dysku
# BASE_DIR = Path(__file__).resolve().parent

# # 2. Sklejamy dokładne ścieżki do plików
# STATS_PATH = BASE_DIR / "data" / "regular_season_stats_from_2010-11_to_2023-24.csv"
# MODELS_PATH = BASE_DIR / "data" / "models_by_season.joblib"
# MATCHUPS_PATH = BASE_DIR / "data" / "playoff_first_round_matchups.json"

# # 3. Wczytujemy pliki używając naszych absolutnych ścieżek
# df_stats = pd.read_csv(STATS_PATH)
# models_dict = joblib.load(MODELS_PATH)

# with open(MATCHUPS_PATH, 'r') as f:
#     matchups = json.load(f)
# result = simulate_whole_playoffs(matchups, "2014-15", df_stats, models_dict)

# print(result)