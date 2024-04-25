import requests
from bs4 import BeautifulSoup

target_url = "https://www.forbes.com/digital-assets/crypto-prices/?sh=1f4266982478"

response = requests.get(target_url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find_all(['td', 'th'])

for tag in table:
    print(tag.text.strip())
