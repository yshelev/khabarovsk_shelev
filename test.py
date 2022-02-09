import requests, json
api_server = 'https://schools.dnevnik.ru/marks.aspx?school=22037&tab=week'


response = requests.get(api_server).json()
