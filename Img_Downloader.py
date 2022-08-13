import requests, bs4, os, sys

try:
    os.mkdir("D:\\jakub\\reddit\\imgur")
except FileExistsError:
    print("Folder już istnieje")
    sys.exit()

search = input(":")
home_url = f"https://imgur.com/search?q={search}"
res_home = requests.get(home_url)
try:
    res_home.raise_for_status()
except Exception as Ex:
    print("Wystąpił błąd:",Ex)
print("Połączono ze stroną")

imgur_soup = bs4.BeautifulSoup(res_home.text,"html.parser")
images = imgur_soup.select('.image-list-link img')

print("Pobieranie zdjęć....")
for img_url in images:
    img_url = img_url.get("src")
    res_img = requests.get(f"https:{img_url}")
    try:
        res_img.raise_for_status()
    except Exception as Ex:
        print("Wystąpił błąd:",Ex)
    imgur_pic = open(f"D:\\jakub\\reddit\\imgur\\{str(img_url).split('/')[3]}",'wb')
    for chunk in res_img.iter_content(10000):
        imgur_pic.write(chunk)
    imgur_pic.close()
print("Pobrano zdjęcia")
    