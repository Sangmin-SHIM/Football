from player.csv_custom import FILE_PLAYER_PATH, read_write_player_list_csv
from club.param_url import find_club_name,all_clubs_list
import os

clubs_list = all_clubs_list()

# ABSOLUTE_FILE_CLUB_PATH
ABSOLUTE_FILE_PLAYER_PATH = os.path.abspath(FILE_PLAYER_PATH)

for enter_club in clubs_list:
    os.chdir(ABSOLUTE_FILE_PLAYER_PATH)  
    club_name = find_club_name(enter_club=enter_club)
    os.chdir(f'{club_name}/')

    df_this_club_players=read_write_player_list_csv(club_name=club_name)

    df_this_club_players.to_csv(f'{club_name}_Players.csv')

    print(f'{club_name} Players Done !')