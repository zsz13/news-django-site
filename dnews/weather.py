import time
import requests
import json

api_key = '1cbb43ff0362f2c578b05fe571c1ea68'
city = 'Almaty'


def get_weather(api_key, city):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Перевести температуру в градусы Цельсия
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None


if __name__ == "__main__":
    # api_key = '1cbb43ff0362f2c578b05fe571c1ea68'
    # city = 'Almaty'
    # while True:  # Создаем бесконечный цикл
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(weather_data)
        # time.sleep(900)
        with open("weather_data.json", "w") as json_file:
            json.dump(weather_data, json_file)

    # weather_data = get_weather(api_key, city)
    # print(weather_data)



# test


# aw = get_weather('1cbb43ff0362f2c578b05fe571c1ea68', 'Almaty')
# print(aw)