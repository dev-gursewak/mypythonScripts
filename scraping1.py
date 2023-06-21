import requests
with requests.Session() as s:
    url = "https://netflix.com"
    r = s.get(url)
    print(r.content)
   
