import requests
from bs4 import BeautifulSoup

messi_url = "https://fbref.com/en/players/d70ce98e/Lionel-Messi"
res = requests.get(messi_url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

goals_table= soup.find("table", attrs={"id":"stats_standard_dom_lg"})
goals_tbody = goals_table.tbody
seasons_stats=goals_tbody.find_all("tr", attrs={"id":"stats"})

print("year     goals")
print("--------------")
for season_stats in seasons_stats:
    year = season_stats.find("th", attrs={"data-stat":"year_id"}).get_text()
    goals= season_stats.find("td", attrs={"data-stat":"goals"}).get_text()
    print(year,"      ",goals)