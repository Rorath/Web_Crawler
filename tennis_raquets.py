from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

scraped_page = requests.get('https://sportstationhk.com/collections/tennis-rackets-%E7%B6%B2%E7%90%83%E6%8B%8D', headers=headers)
soup = BeautifulSoup(scraped_page.content, 'lxml')

racquets_names = []
prices = []

card_info_div = soup.find_all('div' , class_ ='card__information')
for div in card_info_div:
    h3_tag = div.find('h3',class_ = 'card__heading h5')
    if not h3_tag:
        continue
    a_tag = h3_tag.find('a')
    if a_tag and a_tag.text.strip():
        product_name = a_tag.text.strip()
        racquets_names.append(product_name)

prices_tag = soup.find_all('span',class_ = 'price-item price-item--sale price-item--last')
for price in prices_tag:
    prices.append(price.text.strip())

for name,price in zip(racquets_names,prices):
    print('name: ' + name, 'price: ' + price)






