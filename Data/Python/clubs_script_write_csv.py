from club.csv_custom import FILE_CLUB_PATH, write_csv
from club.bs4_custom import get_soup, get_bs4_objects
from club.param_url import get_season, find_league_code, find_league_name, URL_BASE_PATH
from club.merge_csv import make_batch_for_merge_csv_file, execute_batch_for_merged_csv_file
from club.constant import LEAGUES
import os

# User INPUT Variables
# premier_league, ligue_1, bundes_liga, serie_a, la_liga
year = 2012
leagues_list = [league_name for league in LEAGUES for league_name in league.keys()]
period = 10

# ABSOLUTE_FILE_CLUB_PATH
ABSOLUTE_FILE_CLUB_PATH = os.path.abspath(FILE_CLUB_PATH)

for enter_league in leagues_list:
    os.chdir(ABSOLUTE_FILE_CLUB_PATH)    

    year = 2012
    season = get_season(year)
    league_name = find_league_name(enter_league=enter_league)
    

    # Make a folder with league name
    isExistFolder = os.path.exists(league_name)
    if not isExistFolder:
        os.makedirs(league_name)

    league_code = find_league_code(enter_league=enter_league)
    soup = get_soup(league_code=league_code,
                    league_name=league_name,
                    season=season,
                    URL_BASE_PATH=URL_BASE_PATH
                    )
    result = get_bs4_objects(league_name = league_name,
                            league_code=league_code,
                            season = season,
                            soup = soup,
                            )
    clubs = result['clubs']

    # For - {year} ~ {year + 10}
    for year in range(year, year+period):
        # 1) Season
        season = get_season(year)

        # 2) Soup
        soup = get_soup(league_code=league_code,
                    league_name=league_name,
                    season=season,
                    URL_BASE_PATH=URL_BASE_PATH
                    )
        
        this_season=soup.find(attrs={"id":f"results{season}{league_code}1_overall"})
        
        result = get_bs4_objects(league_name = league_name,
                                league_code=league_code,
                                season = season,
                                soup = soup,
                                )
        clubs = result['clubs']
        mps = result['mps']
        ws = result['ws']
        ds = result['ds']
        ls = result['ls']
        pts = result['pts']

        # 3) Csv - each file (multiple)
        write_csv(league_name = league_name,
                season= season,
                clubs = clubs,
                mps = mps,
                ws = ws,
                ds = ds,
                ls = ls,
                pts = pts
                )
        
        # 4) Csv - merged file (single)

    make_batch_for_merge_csv_file(league_name = league_name)
    execute_batch_for_merged_csv_file(league_name = league_name)
