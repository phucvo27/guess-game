from bs4 import BeautifulSoup
import requests

base_url = "http://quotes.toscrape.com"
url = "/page/1"

all_quotes = []
while url:
    res = requests.get(f'{base_url}{url}')
    soup = BeautifulSoup(res.text, 'html.parser')
    quotes = soup.select('.quote')
    print(f'Scraping at {url}')
    for quote in quotes:
        #print(quote.select('span.text')[0].get_text())
        #print(quote.find(class_='text').get_text())
        #print(quote.select('.author')[0].get_text())
        #print(quote.select('a')[0]['href'])
        all_quotes.append({
            "text": quote.find(class_='text').get_text(),
            "author": quote.select('.author')[0].get_text(),
            "bio-link": quote.select('a')[0]['href']
        })
    next_btn = soup.find(class_='next')
    url = next_btn.find('a')['href'] if next_btn else None
print(all_quotes)