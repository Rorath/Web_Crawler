from bs4 import BeautifulSoup
import requests
page_to_scraped = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(page_to_scraped.text, 'html.parser')
print(soup)
tags = soup.find('a',attrs={'class':'tag'})
for tag in tags:
    print(tag.text)
