from inventory import Inventory
from player import Player
from utils import give_name, clear_screen, ANSIColors, draw_hp_bar, frame_text
from locations import LOCATIONS, location_list
from enemies import Enemy, EMEMY_DATABASE
from fight import contr_attack, start_battle, start_boss_fight
from items import ITEMS, list_items
import os
import random
import time


def travel(hero):
    clear_screen()
    print('ЛОКАЦИИ')
    print('--' * 10)
    print('0. Обратно')
    for i, key in enumerate(LOCATIONS):
        if key == 'Цитадель Вечной Силы' and hero.kills < 10:
            continue
        if key == 'Бездна' and hero.boss_die == False:
            continue
        print(f'{i+1}. {key} ')

    print('--' * 10)
    try:
        travel_choice = int(input('Куда путь держишь?: '))
        if travel_choice == 0:
            return
        location = location_list[travel_choice - 1]

        
        
        local_enemy = LOCATIONS[location]['enemies']
        if not local_enemy:
            print (f'{location}. {LOCATIONS[location]["desc"]}')
            print('Нажми Enter чтобы уйти')
            input()
            return
        elif location == 'Цитадель Вечной Силы':
            if hero.kills < 10:
                print('Тебе еще рано сюда...')
                input()
                return
            if hero.boss_die:
                print('Здесь тихо... Жнец душ больше никого не потревожит...')
                input()
                return
            base_enemy = EMEMY_DATABASE['Жнец душ']
            enemy = Enemy(base_enemy.name,base_enemy.max_hp,base_enemy.min_damage, base_enemy.max_damage, base_enemy.reward_gold, base_enemy.reward_xp, base_enemy.on_hit_effect, base_enemy.chance_of_effect, base_enemy.is_boss )
            clear_screen()
            print('Вы входите в Цитадель... Жнец душ ждал вас.')
            input('Нажмите Enter чтобы начать бой')
            start_boss_fight(hero,enemy)
            return
        elif location == 'Бездна' and hero.boss_die == False:
            print('Тебе сюда нельзя. Лучше никогда сюда не приходи...')
            input()
            return
        print (f'{location}. {LOCATIONS[location]["desc"]}')
        input('Нажмите Enter чтобы идти...')
        event_roll = random.randint(1,100)
        if 1 <= event_roll <= 15:
            print('Вы нашли старый сундук!')
            find_gold = random.randint(10, 30)
            hero.gold += find_gold
            print(f'Вы получили {find_gold} золота!')
            input()
            return
        elif 16 <= event_roll <= 26:
            hurt = random.randint(10, 20)
            hero.hp -= hurt
            print(f'Вы попали в ловушку и потеряли {ANSIColors.RED}{hurt}{ANSIColors.RESET}HP!')
            input()
            if not hero.is_alives():
                print('GAME OVER')
                input()
                exit()
            else:
                return
        else:
            local_enemy = LOCATIONS[location]['enemies']
          
            clear_screen()
            input()
            if not local_enemy:
                print('Нажми Enter чтобы уйти')
                input()
                return
            else:
                enemy_name  = random.choice(local_enemy)
                base_enemy = EMEMY_DATABASE[enemy_name]
                enemy = Enemy(base_enemy.name, base_enemy.hp, base_enemy.min_damage,base_enemy.max_damage, base_enemy.reward_gold, base_enemy.reward_xp, base_enemy.on_hit_effect)
                clear_screen()
                print(f'На вас напал {enemy_name}  у него {enemy.hp} здоровья!')
                input('Нажмите Enter чтобы сразиться!')
                start_battle(hero,enemy)

    except  ValueError:
      
        print('Введи правильное число!')
    except IndexError:
        
        print('Такой локации не существует!')
def open_shop(hero):
    while  True:
        clear_screen()
        print('=' * 50)
        print(f'{ANSIColors.YELLOW}|Золота в кошельке: {hero.gold}{ANSIColors.RESET} ')
        print('=' * 50)
        print()
        print(f'{ANSIColors.BOLD}~{ANSIColors.RESET}' * 50)
        print(f'{ANSIColors.BOLD}---------------------МАГАЗИН---------------------{ANSIColors.RESET}')
        print(f'{ANSIColors.BOLD}~{ANSIColors.RESET}' * 50)
        for i, key,  in enumerate(ITEMS, start = 1):
            item_data = ITEMS[key]
            price = ITEMS[key]['price']
            desc = ITEMS[key]['desc']
            print(f'{i}.{ANSIColors.CYAN}{key}{ANSIColors.RESET} - {ANSIColors.YELLOW}{price} золота. {ANSIColors.RESET}({desc})')
        print('0. Выйти')
        print('~' * 50)
        try:
            shop_choice = int(input('Выбери действие: '))
            if shop_choice == 0:
                return
            product = list_items[shop_choice - 1]
            price = ITEMS[product]['price']
            if hero.gold >= price:
                hero.gold -= price
                hero.inventory.add_item(product)
                clear_screen()
                print(f'Вы купили {product}! -{price} золота.')
                input()
            else:
                clear_screen()
                print('Недостаточно золота!')
                input()
        except ValueError:
            clear_screen()
            print('Введи правильное число')
        except IndexError:
            clear_screen()
            print('Нет такого товара!')
            

