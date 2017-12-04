'''https://api.football-data.org/ - это сервис о футболе. Предоставить информацию о ТОП-5 популярных чемпионатах.
Вывести по каждому чемпионату первые пять команд с наибольшим числом забитых голов.'''
#  for python 3.6
import urllib.request
import urllib.error
import json

URL = 'http://api.football-data.org/v1/competitions/'

def get_top_teams_of_leagues():
 #  топ 5 футбольных лиг с сайта http://misto.news/life_hack/top-10-futbolnyh-lig-mira-33864.html
    leagues = [['Английская премьер лига', 445],
               ['Испанская Ла лига', 455],
               ['Немецкая Бундеслига', 452],
               ['Итальянская Серия А', 456],
               ['Французская лига 1', 451]]
    for name_league, code_league in leagues:
        try:
            res = urllib.request.urlopen('{}/{}/leagueTable'.format(URL, code_league))
        except urllib.request.HTTPError as err1:
            print("Ошибка HTTPError: ", err1)
        except urllib.request.URLError as err2:
            print("Ошибка URLError: ", err2)
        else:
            print('\n{}\n'.format(name_league))
            data = json.loads(res.read())
            teams = list([team['teamName'], team['points'], team['goals']] for team in data['standing'])
            teams.sort(key=lambda team: team[1], reverse=True)  # сортировка по очкам
            print('{}\t{}\t{}'.format('Название Команда', 'Количество очков', 'Голы'))
            for name, points, goals in teams[:5]:  # берем первые 5 команд
                print('{}\t{}\t{}'.format(str(name), str(points), str(goals)))


if __name__ == '__main__':
    get_top_teams_of_leagues()
