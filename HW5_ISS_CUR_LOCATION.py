'''http://open-notify.org/Open-Notify-API/ISS-Location-N.. -
это сервис, которые предоставляет информацию о геолокации Международной Космической станции.
Ваша задача за показать в какой точке мира находится станция сейчас.'''

from urllib.request import Request, urlopen
from json import loads

# code for python 3.5
req = Request('http://api.open-notify.org/iss-now.json')
resp = urlopen(req)
res = loads(resp.read().decode('utf-8'))
print('Тек. местоположение МКС \n Широта: {} \n Долгота: {}'.format(res['iss_position']['latitude'],
                                                                        res['iss_position']['longitude']))
