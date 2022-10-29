from csv_custom import FILE_CLUB_PATH, write_csv
from bs4_custom import get_soup, get_bs4_objects
from param_url import get_season, find_league_code, find_league_name, URL_BASE_PATH

# User INPUT Variables
year = 2012
enter_league = "la_liga"
period = 10

# We need these variables for access to site
season = get_season(year)
league_name = find_league_name(enter_league=enter_league)
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

    # 3) Csv
    write_csv(FILE_CLUB_PATH = FILE_CLUB_PATH,
              league_name = league_name,
              season= season,
              clubs = clubs,
              mps = mps,
              ws = ws,
              ds = ds,
              ls = ls,
              pts = pts
              )