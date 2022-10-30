from .constant import LEAGUES
# import datetime

# CURRENT_DAY = datetime.datetime.now()
# CURRENT_YEAR = CURRENT_DAY.year
URL_BASE_PATH = "https://fbref.com/en"

def get_season(year):
    season = f"{year}-{year+1}"
    return season

def find_league_name(enter_league):
    for league in LEAGUES:
        for key in league.keys():
            if key == enter_league:
                league_name = league[key]['name']
                return league_name

def find_league_code(enter_league):
    for league in LEAGUES:
        for key in league.keys():
            if key == enter_league:
                league_code = league[key]['code']
                return league_code

def all_leagues_list():
    ligues=[]
    for league in LEAGUES:
        for key in league.keys():
                ligues.append(key)
    return ligues