import requests
from pprint import pprint
import datetime
open_weather_token = 'token'

def get_weather(city, open_weather_token):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        #pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timesetamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timesetamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        #type_weather = datetime.datetime.fromtimestamp(data['weather']['description'])
        
        print(f'Погода: {city}\nТемпература: {cur_weather}°\n'
        f'Влажность: {humidity}\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n'
        f'Восход солнца: {sunrise_timesetamp}\nЗакат солнца: {sunset_timesetamp}\nПродолжительность дня: {lenght_of_the_day}'
        )
    except Exception as ex:
        print(ex)
        print('Название города неверное')


def main():
    city = input ('Введи город чепушила: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()
