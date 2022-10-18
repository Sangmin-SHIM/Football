import requests
from bs4 import BeautifulSoup

url = "https://fbref.com/en/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element
# print(soup.a.attrs) # a element 의 속성 정보
# print(soup.a["href"]) # a element 의 href 속성 값 정보

# soup.find(attrs={"id":"players"}) 도 가능 # id = "players"인 어떤 element 를 찾기
# players = soup.find("div", attrs={"id":"players"}) # id="players"인 div element 를 찾기
# print(players.get_text()) 

big5 = soup.find(attrs={"id":"big5_table"})

big5_clubs = big5.tbody.find_all(attrs={"class":"left"}) 

for club in big5_clubs:
    print(club.get_text())

######################################
# next_sibling / previous_sibling    #
# => Sibling Node                    #
######################################
print(big5_clubs[3].next_sibling.next_sibling)

##################
# parent         #
# => Parent Node #
##################
print(big5_clubs[3].parent.a.get_text())

#############################################
# find_next_sibling / find_previous_sibling #
#############################################
rk1=big5_clubs[0].find_next_sibling("td")
print(rk1)

######################
# find_next_siblings #
######################
rk1_stats = big5_clubs[0].find_next_siblings("td")
print(rk1_stats)

########
# text #
########
fbref = soup.find_all("a", text="Erling Haaland")
print(fbref)