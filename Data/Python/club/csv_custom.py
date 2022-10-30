import csv
import os

FILE_CLUB_PATH = 'Data/Csv/Bs4_results/Clubs'

def write_csv(**kwargs):
    league_name = kwargs['league_name']
    season = kwargs['season']
    dirs_folder = f'{FILE_CLUB_PATH}/{league_name}'

    clubs = kwargs['clubs']
    mps = kwargs['mps']
    ws = kwargs['ws']
    ds = kwargs['ds']
    ls = kwargs['ls']
    pts = kwargs['pts']

    file = open(f'{league_name}/{season}.csv', 'w',newline='',encoding='utf-8-sig')
    writer = csv.writer(file)

    season_league = [season, league_name]
    writer.writerow(season_league)

    headers = ["Rk", "Club", "Mp", "W", "D", "L", "Pts"]
    writer.writerow(headers)

    for num in range(0, len(clubs)): 
        Rk = num+1
        Club = clubs[num].a.get_text() 
        Mp = mps[num].get_text()
        W = ws[num].get_text()
        D = ds[num].get_text()
        L = ls[num].get_text()
        Pts = pts[num].get_text()
        
        file = open(f'{league_name}/{season}.csv', 'a', newline='', encoding='utf-8-sig')
        writer = csv.writer(file)
        contents = ([Rk, Club, Mp, W, D, L, Pts])
        writer.writerow(contents)
        file.close()    