from club.csv_custom import FILE_CLUB_PATH, read_merged_csv
from club.pandas_custom import drop_duplicate
from league.param_url import find_league_name,all_leagues_list
import os

year = 2002
leagues_list = all_leagues_list()
period = 20

# ABSOLUTE_FILE_CLUB_PATH
ABSOLUTE_FILE_CLUB_PATH = os.path.abspath(FILE_CLUB_PATH)

for enter_league in leagues_list:
    os.chdir(ABSOLUTE_FILE_CLUB_PATH)  
    league_name = find_league_name(enter_league=enter_league)
    os.chdir(f'{league_name}/')
    df_this_league=read_merged_csv(period=period,league_name=league_name)

    df_clubs_list = drop_duplicate(df_original=df_this_league,col_name_1="Club",col_name_2="Link",col_name_3="Club_id",col_name_4="Club_name")

    df_clubs_list.to_csv(f'{league_name}_Clubs.csv', encoding='utf-8-sig')