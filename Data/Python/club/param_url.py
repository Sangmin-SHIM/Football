from club.constant import CLUBS
# import datetime

# CURRENT_DAY = datetime.datetime.now()
# CURRENT_YEAR = CURRENT_DAY.year
URL_BASE_PATH = "https://fbref.com/en"

def find_club_name(enter_club):
    for club in CLUBS:     
        if club == enter_club:
            return CLUBS[enter_club]['Club_name']

def find_club_id(enter_club):
    for club in CLUBS:     
        if club == enter_club:
            return CLUBS[enter_club]['Club_id']

def all_clubs_list():
    clubs=[]
    for club in CLUBS:
        clubs.append(club)
    return clubs