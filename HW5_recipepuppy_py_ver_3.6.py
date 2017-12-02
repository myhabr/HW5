#  http://www.recipepuppy.com/about/api/ - это сервис для получения рецептов.
#  Задача простая: передаем список продуктов, получаем рецепты для этого списка продуктов
#  for python 3.6

import urllib.request
import urllib.error
import json

URL = 'http://www.recipepuppy.com/api/?i='


def get_recipe(*lst_recipes):
    food = ','.join(lst_recipes)
    try:
        req = urllib.request.urlopen(URL + food)
    except urllib.request.HTTPError as err1:
        print("Ошибка HTTPError: ", err1)
    except urllib.request.URLError as err2:
        print("Ошибка URLError: ", err2)
    else:
        recipes = json.loads(req.read())
        for elem in recipes['results']:
            print('Название рецепта: {}\nСсылка: {}\n Ингридиенты:'.format(elem['title'], elem['href']),
                  elem['ingredients'])


if __name__ == '__main__':
    get_recipe('tomato', 'eggs', 'parmesan cheese')
