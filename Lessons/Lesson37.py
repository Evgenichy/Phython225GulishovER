from bs4 import BeautifulSoup
import re
import requests

# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find('div', class_='name')
# row = soup.find_all('div', class_='row')[1].find('div', class_='links').text
# row = soup.find('div', {'class': 'name'})
# row = soup.find('div', {'data-set': 'salary'})
# row = soup.find('div', text='Alena').parent
# row = soup.find('div', text='Alena').find_parent(class_='row')
# row = soup.find('div', id='whois3').find_next_sibling()
# row = soup.find('div', id='whois3').find_previous_sibling()
# print(row)

# def get_copywriter(tag):
#     whois = tag.find('div', {'class': 'whois'}).text
#     if 'Copywriter' in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# copywriter = []
# row = soup.find_all('div', class_='row')
# for r in row:
#     cw = get_copywriter(r)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)


# def get_salary(sy):
#     pattern = r'\d+'
#     # res = re.findall(pattern, sy)[0]
#     res = re.search(pattern, sy).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
# for s in salary:
#     get_salary(s.text)


# r = requests.get('https://ru.wordpress.org/')
# r.encoding = 'utf-8'
# print(r.text)


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('header', {'id': 'masthead'}).find('p', {'class': 'site-title'})
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all('section', {'class': 'plugin-section'})[1]
    plugins = p1.find_all('article')

    for plugin in plugins:
        name = plugin.find('h3').text
        # url = plugin.find('h3').find('a')['href']
        url = plugin.find('h3').find('a')['href']
        print(url)


def main():
    url = 'https://ru.wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()

    #2:25