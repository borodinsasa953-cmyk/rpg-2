from inventory import Inventory
from player import Player
from enemies import Enemy
from locations import LOCATIONS, location_list
from enemies import EMEMY_DATABASE
import random
from utils import  give_name
from game_mechanics import travel

print('Добро пожаловать в RPG 2.0!')
player_name = give_name()
hero = Player(player_name)
game_state = 'main_menu'
while True:
    if game_state == 'main_menu':
        print('=' * 20)
        print('1. Отправиться в путь')
        print('2. Посмотреть характеристики')
        print('3. Выйти')
        print('=' * 20)
        choice = input('Выбери действие: ')
        if choice == '1':
            travel(hero)
        elif choice == '2':
            hero.show_stats()
        elif choice == '3':
            break
        else:
            print('Нет такого действия!')
   