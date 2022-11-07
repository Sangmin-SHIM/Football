from player.csv_custom import FILE_PLAYER_PATH, write_csv
from player.bs4_custom import get_soup, get_bs4_player_objects

from club.param_url import all_clubs_list, find_club_name, find_club_id
from league.param_url import get_season, URL_BASE_PATH
import os

year = 2002
clubs_list = all_clubs_list()
period = 20

# ABSOLUTE_FILE_CLUB_PATH
ABSOLUTE_FILE_CLUB_PATH = os.path.abspath(FILE_PLAYER_PATH)

for enter_club in clubs_list:
    os.chdir(ABSOLUTE_FILE_CLUB_PATH)

    year = 2002
    season = get_season(year)
    club_name = find_club_name(enter_club=enter_club)

    isExistFolder = os.path.exists(club_name)
    if not isExistFolder:
        os.makedirs(club_name)

    club_id=find_club_id(enter_club=enter_club)

    for year in range(year, year+period):
        # 1) Season
        season = get_season(year)

        # 2) Soup
        soup = get_soup(club_id = club_id,
                        club_name = club_name,
                        season = season,
                        path = URL_BASE_PATH
                        )

        result=get_bs4_player_objects(soup=soup)

        if result is None:
            continue

        # 3) Csv - each file (multiple) : PLAYER Data
        write_csv(club_name=club_name,
                 season=season,
                 # Soup Data
                 players=result['players'],
                 nationalities=result['nationalities'],
                 games=result['games'],
                 games_starts=result['games_starts'],
                 minutes=result['minutes'],
                 minutes_90s=result['minutes_90s'],
                 position=result['position'],
                 goals=result['goals'],
                 assists=result['assists'],
                 cards_y=result['cards_y'],
                 cards_r=result['cards_r'],
                 )

        # 4) Csv - merged file (single)
