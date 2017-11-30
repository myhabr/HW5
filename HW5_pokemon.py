#  https://pokeapi.co/ - ПОКЕМОНЫ!!! Тут собрана вся информация о покемонах.
# Необходимо получить номер покемона и выдать краткую информацию о нем.
# for python 3.5

from urllib.request import Request, urlopen
from json import loads

url = 'http://pokeapi.co/api/v2/pokemon/'
pok_numb = input("Ведите ID покемона (целое число): \n")
req = Request(url + pok_numb, headers={'User-Agent': 'Mozilla/5.0'})
resp = urlopen(req)
res = loads(resp.read().decode('utf-8'))

print("Найден покемон: ")
print('Имя покемона: {}'.format(res['name']))
print('Масса: {}'.format(res['weight']))
print('Рост: {}'.format(res['height']) + '\n')
print('Способности:')

for ab_pok in res['abilities']:
    print("Название способности: {}\n Имеет ли инвиз: {}\n".format(ab_pok['ability']['name'], ab_pok['is_hidden']))
