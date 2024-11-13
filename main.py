import requests
from bs4 import BeautifulSoup
import json


data = []

for n in range(1, 11):
    url = f'https://quotes.toscrape.com/page/{n}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        data.append({
            'quote': text,
            'author': author,
            'tags': tags
        })


with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
