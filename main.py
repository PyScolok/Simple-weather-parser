import re

import requests
from bs4 import BeautifulSoup


def get_html(city):
    if re.fullmatch(r'^[a-zA-Zа-яА-Я]+(?:[\s-][a-zA-Zа-яА-Я]+)*$', city):
        response = requests.get(f'https://yandex.ru/search/?text={city}')
        html = response.text
        return html
    else:
        city = input('Название некорректно, попробуйте снова: ')
        get_html(city)


def get_temp(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        temp = soup.find(
            'a', class_='link link_theme_normal ajax i-bem').get_text()
        return temp
    except AttributeError:
        return 'Возникла ошибка, попробуйте позже или проверьте название города...'


city = input("Введите название города: ")
temperature = get_temp(get_html(city))
print(temperature)