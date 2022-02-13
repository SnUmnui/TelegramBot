import requests
from bs4 import BeautifulSoup as bs


def parser_rait():
    college_url = 'http://techcol.lviv.ua'
    url = 'http://techcol.lviv.ua/index.php/studentu'
    html = get_html(url)
    pdf_url = get_pdf_url(html)
    return college_url + pdf_url


def get_html(url):
    r = requests.get(url)
    return r.text


def get_pdf_url(html):
    soup = bs(html, 'html.parser')
    span = soup.find('span', class_='text')
    pdf_url = span.find('a', rel='alternate').get('href')
    return pdf_url
