from player import Player
from utils import give_name
from locations import LOCATIONS, location_list
from enemies import Enemy, EMEMY_DATABASE
import random
def travel(hero):
    print('ЛОКАЦИИ')
    print('--' * 10)
    for i, key in enumerate(LOCATIONS):
        print(f'{i+1}. {key} ')

    print('--' * 10)
    try:
        travel_choice = int(input('Куда путь держишь?: '))
        location = location_list[travel_choice - 1]
        print (f'{location}. {LOCATIONS[location]['desc']}')
    except  ValueError:
        print('Введи правильное число!')
    except IndexError:
        print('Такой локации не существует!')
        

