import requests
from bs4 import BeautifulSoup
import re
import time

from dnews.constants import constants


# Функция для получения курса валюты


def get_currency_rate(url):
    # Получаем содержимое страницы
    response = requests.get(url)

    # Создаем объект BeautifulSoup для парсинга HTML-разметки
    soup = BeautifulSoup(response.content, "html.parser")

    # Получаем элемент с курсом валюты
    result = soup.find("div", class_="BNeawe iBp4i AP7Wnd").get_text()

    # Используем регулярное выражение для извлечения числа из строки
    match = re.search(r"([\d,]+)", result)  # Обратите внимание на запятую

    if match:
        rate_str = match.group(1)
        # Заменяем запятую на точку, если она есть
        rate_str = rate_str.replace(",", ".")
        # Преобразуем в число с плавающей точкой
        return float(rate_str)
    else:
        return None

# Основной код программы


# while True:  # Бесконечный цикл
if __name__ == "__main__":
    usd_url = "https://www.google.com/search?q=курс+доллара+к+тенге"
    current_usd_rate = get_currency_rate(usd_url)
    if current_usd_rate is not None:
        print(f"Текущий курс доллара: {current_usd_rate}")
    else:
        print("Не удалось получить курс доллара")

    eur_url = "https://www.google.com/search?q=курс+евро+к+тенге"
    current_eur_rate = get_currency_rate(eur_url)
    if current_eur_rate is not None:
        print(f"Текущий курс евро: {current_eur_rate}")
    else:
        print("Не удалось получить курс евро")

    rub_url = "https://www.google.com/search?q=курс+рубля+к+тенге"
    current_rub_rate = get_currency_rate(rub_url)
    if current_rub_rate is not None:
        print(f"Текущий курс рубля: {current_rub_rate}")
    else:
        print("Не удалось получить курс рубля")

    # Задержка в 15 минут (900 секунд)
    # time.sleep(900)

    if current_usd_rate is not None:
        constants['usd_rate'] = current_usd_rate

    if current_eur_rate is not None:
        constants['eur_rate'] = current_eur_rate

    if current_rub_rate is not None:
        constants['rub_rate'] = current_rub_rate

    print(constants)