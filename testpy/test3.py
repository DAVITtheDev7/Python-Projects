import requests, sys, webbrowser, bs4

res = requests.get('http://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
LinkElements = soup.select('.r a')
LinkToOpen = min(5, len(LinkElements))

for i in range(LinkToOpen):
    webbrowser.open('http://google.com'+LinkElements[i].get('href'))