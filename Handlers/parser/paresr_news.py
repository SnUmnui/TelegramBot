import requests
import json
from bs4 import BeautifulSoup as bs
from os import path
from os import path

def check_news_update():
    parent_dir = path.dirname(path.abspath(__file__))
    with open(path.join(parent_dir, '', 'news_dict.json'), encoding='utf-8') as file:
         news_dict = json.load(file)

    url = "http://techcol.lviv.ua/"
    r = requests.get(url)

    soup = bs(r.text, "html.parser")
    all_news = soup.find('div', {'id': 'mnwall_iso_container_1'}).find_all('div', {'class': 'mnwall-item'})

    fresh_news = {}
    for new in all_news:
        id_news = new.get('data-id')

        if id_news in news_dict:
            continue
        else:
            url_news = url + new.find('a').get('href')
            title_news = new.find('h3', {'class': 'mnwall-title'}).find('a').text.strip()
            photo_news = new.find('a', {'class': 'mnwall-photo-link'}).find('img').get('src')

            news_dict[id_news] = {
                "url_news": url_news,
                "title_news": title_news,
                "photo_news": photo_news,
             }

            fresh_news[id_news] = {
                "url_news": url_news,
                "title_news": title_news,
                "photo_news": photo_news,
            }

    with open(path.join(parent_dir, '', 'news_dict.json'), "w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return fresh_news
