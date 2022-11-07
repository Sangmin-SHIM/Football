import requests
from bs4 import BeautifulSoup

def get_soup(**kwargs):
    club_id = kwargs['club_id']
    club_name = kwargs['club_name']
    season = kwargs['season']
    path = kwargs['path']

    url = f"{path}/squads/{club_id}/{season}/{club_name}-Stats"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    return soup

def get_bs4_player_objects(**kwargs):
    soup = kwargs['soup']

    # Club for Players
    if soup.find(attrs={'id':"all_stats_standard"}) is not None:
        this_club=soup.find(attrs={'id':"all_stats_standard"})
        table = this_club.tbody
    else:
        return None

    # Data we want to get 
    players = table.find_all(attrs={'data-stat':'player'})
    nationalities = table.find_all(attrs={'data-stat':'nationality'})
    games = table.find_all(attrs={'data-stat':'games'})
    position = table.find_all(attrs={'data-stat':'position'})
    games_starts = table.find_all(attrs={'data-stat':'games_starts'})
    minutes = table.find_all(attrs={'data-stat':'minutes'})
    minutes_90s = table.find_all(attrs={'data-stat':'minutes_90s'})
    goals = table.find_all(attrs={'data-stat':'goals'})
    assists = table.find_all(attrs={'data-stat':'assists'})
    cards_y = table.find_all(attrs={'data-stat' : 'cards_yellow'})
    cards_r = table.find_all(attrs={'data-stat' : 'cards_red'})

    # Result 
    result = {'players' : players,
              'nationalities' : nationalities,
              'games' : games,
              'position':position,
              'games_starts' : games_starts,
              'minutes' : minutes,
              'minutes_90s' : minutes_90s,
              'goals' : goals,
              'assists' : assists,
              'cards_y' : cards_y,
              'cards_r' : cards_r,
              }

    return result

