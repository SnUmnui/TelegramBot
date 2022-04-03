#pip install requests
#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup as bs


def parser_pdf(search_item, who = 'abituriientu'):
    college_url = 'http://techcol.lviv.ua'
    url = f'http://techcol.lviv.ua/index.php/{who}'
    html = get_html(url)
    pdf_url = get_pdf_url(html, search_item)
    return college_url + pdf_url


def get_html(url):
    r = requests.get(url)
    return r.text


def get_pdf_url(html, search_item):
    soup = bs(html, 'html.parser')
    span = soup.find('span', id=f"{search_item}")
    pdf_url = span.find('a').get('href')
    return pdf_url
