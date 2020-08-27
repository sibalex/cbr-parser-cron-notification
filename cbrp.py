import requests  # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import os
from datetime import datetime
# sudo chmod a+x cbrp.py
# env -i /bin/bash/ --noprofile --norc


def get_html():
    url = 'http://www.cbr.ru/'
    r = requests.get(url)
    return r.text


def get_dollar(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', attrs={'class':'col-6 ml-auto col-md-2'}).get_text().replace('₽','').replace('\n','')
    return content


def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s]))) # brew install terminal-notifier


def main():
    rate = get_dollar(get_html())
    notify(title = "Dollar USA", subtitle = rate + " ₽", message  = '{}'.format(datetime.today()))


if __name__ == '__main__':
    main()
