import pandas as pd
import csv

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

def read_merged_csv(**kwargs):
    period = kwargs['period']
    league_name = kwargs['league_name']
    merged_file_name = f'{league_name}_merged'

    df_this_league = pd.read_csv(f'{merged_file_name}.csv')

    # Clean(Remove) data like - "2012-2013 xx League", "Rk, W, D, S" 
    skipped_row=[]
    total_row=len(df_this_league.index)
    skipped_value = int(total_row/period)
    for row in range(0,total_row+1,skipped_value):
        skipped_row.append(row)
    
    df_this_league = pd.read_csv(f'{merged_file_name}.csv', skiprows=skipped_row)

    return df_this_league