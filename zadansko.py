import bs4, requests
exampleFile = open("example.html")
example = bs4.BeautifulSoup(exampleFile, "html.parser")
print(type(example))
elementy = example.select("#author")
print(elementy[0].text)
print(elementy[0].attrs)
print(elementy[0].get("id"))
elementy_p = example.select("p")
for element in elementy_p:
    print(element)