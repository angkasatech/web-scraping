import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/'
contents = requests.get(url)
#print(contents.text)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
data = data[0]

shalat = {}
i = 0
for d in data:
    if i == 1:
        shalat['subuh'] = d.get_text()
    elif i == 2:
        shalat['dzuhur'] = d.get_text()
    elif i == 3:
        shalat['ashar'] = d.get_text()
    elif i == 4:
        shalat['maghrib'] = d.get_text()
    elif i == 5:
        shalat['isya'] = d.get_text()
    i += 1

print(shalat)

print(shalat['subuh'])