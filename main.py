import os
import sys
from inventory import Inventory
from player import Player
from enemies import Enemy
from locations import LOCATIONS, location_list
from enemies import EMEMY_DATABASE
import random
from utils import  give_name, clear_screen, ANSIColors
from game_mechanics import travel, open_shop, start_battle
from shop import shop_items, list_shop_items
from save_system import load_game, save_game
import time
os.system('')
sys.stdout.reconfigure(encoding='utf-8')

print("""
\033[93m╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║\033[91m   ██████╗ ██████╗  ██████╗\033[93m                                   ║
║\033[91m   ██╔══██╗██╔══██╗██╔════╝\033[93m                                   ║
║\033[38;5;208m   ██████╔╝██████╔╝██║  ███╗\033[93m                                  ║
║\033[38;5;208m   ██╔══██╗██╔═══╝ ██║   ██║\033[93m                                  ║
║\033[93m   ██║  ██║██║     ╚██████╔╝\033[93m                                  ║
║\033[93m   ╚═╝  ╚═╝╚═╝      ╚═════╝\033[93m                                   ║
║                                                              ║
║\033[96m            Т Е К С Т О В А Я   Р П Г\033[93m                         ║
║\033[97m                   v 2.0\033[93m                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝\033[0m
""")
hero =  None

print('1. Новая игра')
print('2. Загрузить игру')
main_choice = input('Выбери действие: ')

if main_choice == '2':
    hero = load_game()
    input()
if hero is None:
    
    player_name = give_name()
    hero = Player(player_name)

game_state = 'main_menu'
while True:

    if game_state == 'main_menu':
        clear_screen()
        print('=' * 30)
        print('1. Отправиться в путь')
        print('2. Посмотреть характеристики')
        print('3. Зайти в магазин')
        print('4. Инвентарь')
        print('5. Сохранить игру')
        print('0. Выйти')
        print('=' * 30)
        choice = input('Выбери действие: ')
        if choice == '1':
            travel(hero)
        elif choice == '2':
            clear_screen()
            hero.show_stats()
            input()
        elif choice == '3':
            open_shop(hero)
        elif choice == '4':
            clear_screen()
            hero.inventory.show_items()
            item_choice = input('Что вы хотите экипировать?: ')
            hero.equip_item(item_choice)
        elif choice == '5':
            save_game(hero)
            input()
        elif choice == '0':
            break
        else:
            print('Нет такого действия!')
   