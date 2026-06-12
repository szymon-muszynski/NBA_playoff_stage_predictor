import random

def get_home_team_win_chance(home_team, away_team):
    pass

def simulate_single_match(home_team_win_chance):
    return random.random() < home_team_win_chance


def simulate_single_series(home_team, away_team):
    
    home_team_score = 0
    away_team_score = 0
    
    home_team_win_chance = get_home_team_win_chance(home_team = home_team,away_team=away_team)
    
    while True:
        if simulate_single_match(home_team_win_chance):
            home_team_score+=1
        else:
            away_team_score+=1
            
        if home_team_score == 4:
            return home_team
        elif away_team_score == 4:
            return away_team