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
        if players[num].a != None:
            Link = players[num].a['href']

            player_identifier = players[num].a['href'].strip("/en/players/").split('/')
            Player_id = player_identifier[0]
            Player_name = player_identifier[1]

        file = open(f'{club_name}/{season}.csv', 'a', newline='', encoding='utf-8-sig')
        writer = csv.writer(file)
        contents = ([Player, Nationality, Position, Game, Game_start, Assist, Goal,
                     Minute, Minute_90s, Yellow_card, Red_card, Link, Player_id, Player_name])
        writer.writerow(contents)
        file.close()  
