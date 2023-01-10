from player.csv_custom import FILE_PLAYER_PATH
from club.param_url import find_club_name,all_clubs_list
import os
import pandas as pd

clubs_list = all_clubs_list()

# ABSOLUTE_FILE_CLUB_PATH
ABSOLUTE_FILE_PLAYER_PATH = os.path.abspath(FILE_PLAYER_PATH)

df_list=[]
for enter_club in clubs_list:
    os.chdir(ABSOLUTE_FILE_PLAYER_PATH)  
    club_name = find_club_name(enter_club=enter_club)
    os.chdir(f'{club_name}/')

    df_this_club_players=pd.read_csv(f'{club_name}_Players.csv')
    df_this_club_players=df_this_club_players[["Player","Link","Player_name","Player_id","Nationality","Position","club"]]
    # If player has more than two positions or two club, then the id has been created for same player,
    # We have to remove this duplicated. It can be done very simply in excel, with 
    # ["Player","Link","Player_name","Player_id","Nationality"]

    df_list.append(df_this_club_players)
    print(f'{enter_club} appended !')

df_all_players = pd.concat(df_list).drop_duplicates().reset_index(drop=True)


# /All-Players
os.chdir(f'{ABSOLUTE_FILE_PLAYER_PATH}/All-Players')  
df_all_players.to_csv("All_Players.csv", encoding="utf-8-sig")
print("-------------------")
print("All Players saved !")
print("-------------------")
