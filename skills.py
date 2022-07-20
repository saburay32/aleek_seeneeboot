import os, webbrowser, sys, requests, subprocess
import voice

try:
	import requests		#pip install requests
except:
	pass


def browser():
    webbrowser.open('https://yandex.ru/', new=2)
    #print('браузер запущен')

def game():
    try:
        # subprocess.Popen('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/JetBrainspycharm64.exe')
        subprocess.Popen('C:/Program Files/JetBrains/PyCharm Community Edition 2021.2/bin/pycharm64.exe')
        voice.speaker('Путь к файлу найден ')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


    #print('игра запущена')

def offpc():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    # os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')

def weather():
    try:
        params = {'q': 'Stupino', 'units': 'metric', 'lang': 'ru', 'appid': 'dc40f5e3aa2cf7cebf4320f11663bef5'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    sys.exit()

def passiwe():
    pass
