from bs4 import BeautifulSoup
import requests
import re
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find('div', {'class': 'stat mB6'})
    th = t.find_all('thead')
    tb = t.find_all('tbody')
    # print(th)

    for thead in th:
        td = thead.find_all('span')
        for index in range(len(td)):
            print(td[index].text, end=' ')
        # print(td)

    for tbody in tb:
        td = tbody.find_all('td')
        for index in range(len(td)):
            print(td[index].text, end=' ')
        # print(td)


def main():
    url = 'https://www.sports.ru/rfpl/table/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
