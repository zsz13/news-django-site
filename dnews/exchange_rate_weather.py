import time
import requests
from bs4 import BeautifulSoup
import re
import json


def get_currency_rate(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find("div", class_="BNeawe iBp4i AP7Wnd").get_text()
    match = re.search(r"([\d,]+)", result)

    if match:
        rate_str = match.group(1)
        rate_str = rate_str.replace(",", ".")
        return float(rate_str)
    else:
        return None


def get_weather(api_key, city):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None


if __name__ == "__main__":
    api_key = '1cbb43ff0362f2c578b05fe571c1ea68'
    city = 'Almaty'

    while True:
        usd_url = "https://www.google.com/search?q=курс+доллара+к+тенге"
        current_usd_rate = get_currency_rate(usd_url)
        eur_url = "https://www.google.com/search?q=курс+евро+к+тенге"
        current_eur_rate = get_currency_rate(eur_url)
        rub_url = "https://www.google.com/search?q=курс+рубля+к+тенге"
        current_rub_rate = get_currency_rate(rub_url)

        weather_data = get_weather(api_key, city)

        if current_usd_rate is not None:
            print(f"Текущий курс доллара: {current_usd_rate}")

        if current_eur_rate is not None:
            print(f"Текущий курс евро: {current_eur_rate}")

        if current_rub_rate is not None:
            print(f"Текущий курс рубля: {current_rub_rate}")

        if weather_data:
            print(weather_data)

        data = {
            'usd_rate': current_usd_rate if current_usd_rate is not None else "N/A",
            'eur_rate': current_eur_rate if current_eur_rate is not None else "N/A",
            'rub_rate': current_rub_rate if current_rub_rate is not None else "N/A",
            'weather_data': weather_data if weather_data else "N/A"
        }

        with open("currency_rate_weather.json", "w") as json_file:
            json.dump(data, json_file)

        time.sleep(900)
