import requests

class SiteRequests(requests.Response):
    def __init__(self, name):
        self.name = name

    def get_link(self)->str:
        return f"https://{self.name}.com"
    
    def get_status(self)->int:
        get_link = requests.get(self.get_link())
        return get_link.status_code

    def status_ok(self):
        if self.get_status() == requests.codes.ok:
            print("Access OK")
        else:
            print("Access Denied")
    
# naver = SiteRequests("naver")
# fbref = SiteRequests("fbref")

# print(naver.get_link())
# print(naver.get_status())
# print(naver.status_ok())

# print(fbref.get_link())
# print(fbref.get_status())
# print(fbref.status_ok())

# 10/10/2022, 36:28 ~ (raise_for_status())

res = requests.get("https://fbref.com")
res.raise_for_status()
print(len(res.text))

with open("fbref.html", "w", encoding="utf8") as file:
    file.write(res.text)
    