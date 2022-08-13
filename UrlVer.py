import requests, bs4,sys
home_url = "https://ekonomik.gniezno.pl"
false_urls = []
print(f"Łączenie ze stroną domową {home_url}.....")
res_home = requests.get(home_url)
try:
    res_home.raise_for_status()
except:
    sys.exit()
soup_home = bs4.BeautifulSoup(res_home.text,'html.parser')
links =  soup_home.select('a[href]')
for i in range(len(links)+ 1):
    if i > (len(links) - 1):
        url = "https://ekonomik.gniezno.pl/Nie_istnieje"
    else:
        url = links[i].get('href')
    print(f"Łączenie ze stroną {url}.....")
    try:
        res = requests.get(url)
    except:
        print("Pominięto.")
        continue
    try:
        res.raise_for_status()
    except:
        if res.status_code == 404:
            false_urls.append({res.status_code:url})
        continue
print(false_urls)