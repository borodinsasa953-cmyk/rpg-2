from inventory import Inventory
from player import Player
from utils import give_name
from locations import LOCATIONS, location_list
from enemies import Enemy, EMEMY_DATABASE
from shop import shop_items, list_shop_items
import random

def start_battle(hero, enemy):
    print(f'Бой начался! {hero.name} против {enemy.name}!')
    while hero.is_alives() and enemy.is_alive():
        print(f'Ваше здоровье: {hero.hp} HP')
        print(f'Здоровье противника ({enemy.name}): {enemy.hp} HP')
        
        print('1. Ударить' )
        print('2. Выпить зелье')
        battle_choice = input('Твое действие: ')
        if battle_choice == '1':
            damage = random.randint(hero.min_damage, hero.max_damage)
            print(f'Вы ударили врага на {damage} урона!')
            enemy.take_damage(damage)
            if not enemy.is_alive():
                print(f'Вы победили {enemy.name}! ')
                hero.gold += enemy.reward_gold
                hero.xp += enemy.reward_xp
                hero.kills += 1
                print(f'Вы получили {enemy.reward_gold} золота и {enemy.reward_xp} опыта!')
                input()
                break
        elif battle_choice == '2':
            if hero.inventory.items.get('Зелье', 0) > 0:
                hero.inventory.remove_item('Зелье') 
                hero.heal(20)
                print('Вы полечились на 20 HP')
                input()
                continue
            else:
                print('У вас нет зелий!')
                input()
                continue
        print('Противник атакует! ')
        hero.take_damage(random.randint(enemy.min_damage, enemy.max_damage))
        if not hero.is_alives():
            print('GAME OVER')
            input()
            break
        



def travel(hero):
    print('ЛОКАЦИИ')
    print('--' * 10)
    print('0. Обратно')
    for i, key in enumerate(LOCATIONS):
        print(f'{i+1}. {key} ')

    print('--' * 10)
    try:
        travel_choice = int(input('Куда путь держишь?: '))
        if travel_choice == 0:
            return
        location = location_list[travel_choice - 1]
        local_enemy = LOCATIONS[location]['enemies']
        print (f'{location}. {LOCATIONS[location]["desc"]}')
        input()
        if not local_enemy:
            print('Нажми Enter чтобы уйти')
            input()
            return
        else:
            enemy_name  = random.choice(local_enemy)
            base_enemy = EMEMY_DATABASE[enemy_name]
            enemy = Enemy(base_enemy.name, base_enemy.hp, base_enemy.min_damage,base_enemy.max_damage, base_enemy.reward_gold, base_enemy.reward_xp)
            print(f'На вас напал {enemy_name}  у него {enemy.hp} здоровья!')
            input('Нажмите Enter чтобы сразиться!')
            start_battle(hero,enemy)

    except  ValueError:
        print('Введи правильное число!')
    except IndexError:
        print('Такой локации не существует!')
def open_shop(hero):
    while  True:
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
                print(f'Вы купили {product}! -{price} золота.')
                input()
            else:
                print('Недостаточно золота!')
                input()
        except ValueError:
            print('Введи правильное число')
        except IndexError:
            print('Нет такого товара!')
                

