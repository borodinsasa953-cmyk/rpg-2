from inventory import Inventory
from player import Player
from utils import give_name, clear_screen, ANSIColors, draw_hp_bar
from locations import LOCATIONS, location_list
from enemies import Enemy, EMEMY_DATABASE
from shop import shop_items, list_shop_items
import os
import random
import time
def start_battle(hero, enemy):
    clear_screen()
    print('=' * 40)
    print(f'⚔️   БОЙ:{ANSIColors.GREEN} {hero.name} {ANSIColors.RESET}  против {ANSIColors.RED}{enemy.name}{ANSIColors.RESET}')
    print('=' * 40)
    input()
    
    while hero.is_alives() and enemy.is_alive():
        clear_screen()
        print('=' * 40)
        print(f'Вы {ANSIColors.GREEN}({hero.name}){ANSIColors.RESET}: {draw_hp_bar(hero.hp, hero.max_hp)}')
        print(f'Враг {ANSIColors.RED}({enemy.name}){ANSIColors.RESET}: {draw_hp_bar(enemy.hp, enemy.max_hp)}')
        print('=' * 40)
        
        
        print(f'1. {ANSIColors.RED}Ударить{ANSIColors.RESET}' )
        print(f'2. {ANSIColors.PURPLE}Выпить зелье{ANSIColors.RESET}')
        battle_choice = input('Твое действие: ')
        if battle_choice == '1':
            damage = random.randint(hero.min_damage, hero.max_damage)
            if hero.weapon ==  'Меч':
                damage += 5
            clear_screen()
            time.sleep(1)
            print(f'Вы ударили врага на {damage} урона!')
            enemy.take_damage(damage)
            if not enemy.is_alive():

                if enemy.name == 'Жнец душ':

                    clear_screen()
                    time.sleep(0.5)
                    print('='* 40)
                    print('ВЫ ПОБЕДИЛИ БОССА И СПАСЛИ МИР!')
                    print('='* 40)
                    exit()
                else:
                    clear_screen()
                    time.sleep(1)
                    print(f'Вы победили {enemy.name}! ')
                    hero.gold += enemy.reward_gold
                    hero.xp += enemy.reward_xp
                    hero.kills += 1
                    print(f'Вы получили {enemy.reward_gold} золота и {enemy.reward_xp} опыта!')
                    hero.check_level_up()
                    input()
                    break
        elif battle_choice == '2':
            if hero.inventory.items.get('Зелье', 0) > 0:
                hero.inventory.remove_item('Зелье') 
                hero.heal(20)
                clear_screen()
                time.sleep(0.5)
                print('Вы полечились на 20 HP')
                input()
                continue
            else:
                clear_screen()
                time.sleep(0.5)
                print('У вас нет зелий!')
                input()
                continue
        clear_screen()
        print('Противник атакует! ')
        time.sleep(1)
        damage = random.randint(enemy.min_damage, enemy.max_damage)
        if hero.armor == 'Броня':
            damage = max(1, damage - 5)
        hero.take_damage(damage)
        if not hero.is_alives():
            clear_screen()
            print('GAME OVER')
            input()
            break
        



def travel(hero):
    clear_screen()
    print('ЛОКАЦИИ')
    print('--' * 10)
    print('0. Обратно')
    for i, key in enumerate(LOCATIONS):
        if key == 'Цитадель Вечной Силы' and hero.kills < 3:
            continue
        print(f'{i+1}. {key} ')

    print('--' * 10)
    try:
        travel_choice = int(input('Куда путь держишь?: '))
        if travel_choice == 0:
            return
        location = location_list[travel_choice - 1]
        local_enemy = LOCATIONS[location]['enemies']
        if location == 'Цитадель Вечной Силы' and hero.kills < 3:
            clear_screen()
            print('Сначала наберись опыта. Закрыто.')
            input()
        else:
            clear_screen()
            print (f'{location}. {LOCATIONS[location]["desc"]}')
            input()
            if not local_enemy:
                clear_screen()
                print('Нажми Enter чтобы уйти')
                input()
                return
            else:
                enemy_name  = random.choice(local_enemy)
                base_enemy = EMEMY_DATABASE[enemy_name]
                enemy = Enemy(base_enemy.name, base_enemy.hp, base_enemy.min_damage,base_enemy.max_damage, base_enemy.reward_gold, base_enemy.reward_xp)
                clear_screen()
                print(f'На вас напал {enemy_name}  у него {enemy.hp} здоровья!')
                input('Нажмите Enter чтобы сразиться!')
                start_battle(hero,enemy)

    except  ValueError:
        clear_screen()
        clear_screen()
        print('Введи правильное число!')
    except IndexError:
        clear_screen()
        clear_screen()
        print('Такой локации не существует!')
def open_shop(hero):
    while  True:
        clear_screen()
        print(f'Золота в кошельке: {hero.gold} ')
        for i, key,  in enumerate(shop_items, start = 1):
            price = shop_items[key]['price']
            desc = shop_items[key]['desc']
            print(f'{i}. {key}, - {price} золота. ({desc})')
        print('0. Выйти')
        try:
            shop_choice = int(input('Выбери действие: '))
            if shop_choice == 0:
                return
            product = list_shop_items[shop_choice - 1]
            price = shop_items[product]['price']
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
                

