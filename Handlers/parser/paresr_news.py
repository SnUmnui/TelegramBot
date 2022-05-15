import requests
import json
from bs4 import BeautifulSoup as bs

def parser_news():
    url = 'http://techcol.lviv.ua/'
    html = get_html(url)
    news_dict = get_all_news(html, url)

    return news_dict

def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_news(html, url):
    soup = bs(html, 'html.parser')
    all_news = soup.find('div', {'id': 'mnwall_iso_container_1'}).find_all('div', {'class': 'mnwall-item'})
    news_dict = {}

    for new in all_news:
        id_news = new.get('data-id')
        url_news = url + new.find('a').get('href')
        title_news = new.find('h3', {'class': 'mnwall-title'}).find('a').text.strip()
        photo_news = new.find('a', {'class': 'mnwall-photo-link'}).find('img').get('src')

        news_dict[id_news] = {
            "url_news": url_news,
            "titel_news": title_news,
            "photo_news": photo_news,
        }

    with open("news_dict.json", "w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)
    return news_dict

print(parser_news())