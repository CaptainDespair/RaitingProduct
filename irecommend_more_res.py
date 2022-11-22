import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

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
        start_time = time.time()
        counter = 0
   # try:
        soup = BeautifulSoup(html.text, 'lxml')
        for titles in soup.find_all("div", {"class":'ProductTizer plate teaser-item'}):
            for title in titles.find("div", {"class":"title"}):
                print("Название:", title.text)
                counter += 1
            for raitings in titles.find(class_="average-rating").find('span'):
                print("Оценка:", raitings.text)
            for votes in titles.find(class_ = "read-all-reviews-link").find(class_ ="counter"):
                print("Голосов:", votes.text)
        print("------------------------")
        print("Выполнено за ~ {} секунд ".format(time.time() - start_time))
        return f'Найдено результатов >= {counter}'
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