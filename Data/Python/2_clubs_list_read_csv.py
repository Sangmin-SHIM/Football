import pandas as pd
from club.constant import LEAGUES
from club.csv_custom import FILE_CLUB_PATH, read_merged_csv
from club.pandas_custom import drop_duplicate
from club.param_url import find_league_name
import os

year = 2002
leagues_list = [league_name for league in LEAGUES for league_name in league.keys()]
period = 20

# ABSOLUTE_FILE_CLUB_PATH
ABSOLUTE_FILE_CLUB_PATH = os.path.abspath(FILE_CLUB_PATH)

for enter_league in leagues_list:
    os.chdir(ABSOLUTE_FILE_CLUB_PATH)  
    league_name = find_league_name(enter_league=enter_league)
    os.chdir(f'{league_name}/')
    df_this_league=read_merged_csv(period=period,league_name=league_name)

    df_clubs_list = drop_duplicate(df_original=df_this_league,col_name="Club")

    df_clubs_list.to_csv(f'{league_name}_Clubs.csv')