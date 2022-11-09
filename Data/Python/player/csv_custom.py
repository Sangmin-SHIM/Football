import pandas as pd
import csv
import re


FILE_PLAYER_PATH = 'Data/Csv/Bs4_results/Players'

def write_csv(**kwargs):
    club_name = kwargs['club_name']
    season = kwargs['season']
    # Soup Data
    players=kwargs['players']
    nationalities=kwargs['nationalities']
    games=kwargs['games']
    games_starts=kwargs['games_starts']
    minutes=kwargs['minutes']
    minutes_90s=kwargs['minutes_90s']
    positions=kwargs['position']
    goals=kwargs['goals']
    assists=kwargs['assists']
    cards_y=kwargs['cards_y']
    cards_r=kwargs['cards_r']

    file = open(f'{club_name}/{season}.csv', 'w',newline='',encoding='utf-8-sig')
    writer = csv.writer(file)

    season_club = [season, club_name]
    writer.writerow(season_club)

    headers = ["Player", "Nationality", "Position" ,"Game", "Games Starts", "Assists", "Goals", "Minutes", "Minutes 90s",
               "Yellow Card", "Red Card","Link", "Player_id", "Player_name"]
    writer.writerow(headers)

    for num in range(0, len(players)):
        Player = players[num].get_text()
        Nationality = nationalities[num].get_text()
        Position = positions[num].get_text()
        Game = games[num].get_text()
        Game_start = games_starts[num].get_text()
        Assist=assists[num].get_text()
        Goal=goals[num].get_text()
        Minute=minutes[num].get_text()
        Minute_90s=minutes_90s[num].get_text()
        Yellow_card=cards_y[num].get_text()
        Red_card=cards_r[num].get_text()

        Link = 'No detected'
        Player_id = ''
        Player_name = ''
        base_url = re.compile("^/en/players/") 

        if players[num].a != None:
            Link = players[num].a['href']
            delete_this_url = base_url.match(Link).group()


            player_identifier = re.sub(delete_this_url,"",Link).split('/')
            Player_id = player_identifier[0]
            Player_name = player_identifier[1]

        file = open(f'{club_name}/{season}.csv', 'a', newline='', encoding='utf-8-sig')
        writer = csv.writer(file)
        contents = ([Player, Nationality, Position, Game, Game_start, Assist, Goal,
                     Minute, Minute_90s, Yellow_card, Red_card, Link, Player_id, Player_name])
        writer.writerow(contents)
        file.close()  


def read_merged_csv(**kwargs):
    period = kwargs['period']
    club_name = kwargs['club_name']
    merged_file_name = f'{club_name}_merged'

    df_this_club = pd.read_csv(f'{merged_file_name}.csv')

    # Clean(Remove) data like - "2012-2013 xx League", "Rk, W, D, S" 
    skipped_row=[]
    total_row=len(df_this_club.index)
    skipped_value = int(total_row/period)
    for row in range(0,total_row+1,skipped_value):
        skipped_row.append(row)
    
    df_this_club = pd.read_csv(f'{merged_file_name}.csv', skiprows=skipped_row)

    # Delete the row written 'Club'
    mask = df_this_club['Player'].isin(['Player'])
    df_this_club = df_this_club[~mask]
    return df_this_club

def read_write_player_list_csv(**kwargs):
    club_name = kwargs['club_name']

    df=pd.read_csv(f'{club_name}_Players.csv')
    df_link=df[["Player","Link"]]

    player_list=[df_link.loc[num].to_list()[0] for num in range (0,len(df_link))]
    link_list=[df_link.loc[num].to_list()[1] for num in range (0,len(df_link))]
    player_name_list=[]
    player_id_list=[]

    base_url = re.compile("^/en/players/") 

    for link in link_list:
        delete_this_url = base_url.match(link).group()
        player_identifier = re.sub(delete_this_url,"",link).split('/')
        player_id = player_identifier[0]
        player_name = player_identifier[1]
        
        if link == "No detected":
            player_name_list.append("No detected")
            player_id_list.append("No detected")
            
        player_name_list.append(player_name)
        player_id_list.append(player_id)

    df_player = pd.DataFrame(
        {'Player': player_list,
        'Link' : link_list,
        'Player_name(param)': player_name_list,
        'Player_id(param)': player_id_list
        })
    
    return df_player