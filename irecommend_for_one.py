import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from threading import Thread


def search_pattern(url, user_query):     
    url_query = user_query.replace(' ', '%20')                     
    new_url = ''.join([url, url_query])
    return new_url


def get_html(new_url):
    ua = UserAgent()
    headers = "'" + ua.random + "'"
    html = requests.get(new_url, headers={'User-agent': headers}, timeout=10)
    return html


def html_data(html):
   # try:
        soup = BeautifulSoup(html.text, 'lxml')
        def titles():
            for titles in soup.find_all("div", {"class":'title'}):
                print(titles.text)
        def raitings():
            for raitings in soup.find_all(class_="average-rating"):
                print(raitings.text)
        def votes():
            for votes in soup.find_all(class_ = "read-all-reviews-link"):
                print(votes.text)
        
        return titles(), raitings(), votes()
    
    #except:
     #   return ('Error!')
    

def main():
    url = 'https://irecommend.ru/srch?query='
    user_query = input('Введите название товара: ')
    print(
        html_data(
            get_html(
                (search_pattern(url, user_query))
            )
        )
    )


if __name__ == '__main__':
    main()