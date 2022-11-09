from player.csv_custom import FILE_PLAYER_PATH, read_merged_csv
from player.pandas_custom import drop_duplicate
from club.param_url import find_club_name,all_clubs_list
import os

year = 2002
clubs_list = all_clubs_list()
period = 20

# ABSOLUTE_FILE_CLUB_PATH
ABSOLUTE_FILE_PLAYER_PATH = os.path.abspath(FILE_PLAYER_PATH)

for enter_club in clubs_list:
    os.chdir(ABSOLUTE_FILE_PLAYER_PATH)  
    club_name = find_club_name(enter_club=enter_club)
    os.chdir(f'{club_name}/')
    df_this_club=read_merged_csv(period=period,club_name=club_name)

    df_players_list = drop_duplicate(df_original=df_this_club,col_name_1="Player",col_name_2="Link",col_name_3="Player_id",col_name_4="Player_name")

    df_players_list.to_csv(f'{club_name}_Players.csv')