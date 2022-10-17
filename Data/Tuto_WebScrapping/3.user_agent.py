import requests

url = "https://fbref.com"
# User Agent String - 403 에러 코드가 나지 않고, 200 코드가 뜨면서 작동이 되어야 한다.
# 그런데 이상하게도 headers 값을 넣으니 오히려 작동이 되지 않는다.
# 이 사이트에 들어가기 위해서 headers 값을 지우고 작동시키면 된다.
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)

res.raise_for_status()
print(len(res.text))

with open("fbref1.html", "w", encoding="utf8") as file:
    file.write(res.text)
    