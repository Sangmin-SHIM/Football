import requests
from bs4 import BeautifulSoup

def get_soup(**kwargs):
    league_code = kwargs['league_code']
    league_name = kwargs['league_name']
    season = kwargs['season']
    path = kwargs['path']

    url = f"{path}/comps/{league_code}/{season}/{season}-{league_name}-Stats"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    return soup

def get_bs4_club_objects(**kwargs):
    season=kwargs['season']
    soup = kwargs['soup']
    league_code = kwargs['league_code']

    # League for Clubs
    this_season=soup.find(attrs={"id":f"results{season}{league_code}1_overall"})

    # Data we want to get 
    clubs = this_season.find_all("td", attrs={"data-stat" : "team"})
    mps = this_season.find_all("td", attrs={"data-stat" : "games"})
    ws = this_season.find_all("td", attrs={"data-stat" : "wins"})
    ds = this_season.find_all("td", attrs={"data-stat" : "ties"})
    ls = this_season.find_all("td", attrs={"data-stat" : "losses"})
    pts = this_season.find_all("td", attrs={"data-stat" : "points"})

    # Result
    result = {'clubs' : clubs,
              'mps' : mps,
              'ws' : ws,
              'ds' : ds,
              'ls' : ls,
              'pts' : pts
              }

    return result

