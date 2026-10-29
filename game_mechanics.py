from player import Player
from utils import give_name
from locations import LOCATIONS, location_list
from enemies import Enemy, EMEMY_DATABASE
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
            print(f'Вы ударили врага на {hero.damage} урона!')
            enemy.take_damage(hero.damage)
            if not enemy.is_alive():
                print(f'Вы победили {enemy.name}! ')
                input()
                break
        print('Противник атакует! ')
        enemy.attack(hero)
        if not hero.is_alives:
            print('GAME OVER')
            input()
            break
        

       



def travel(hero):
    print('ЛОКАЦИИ')
    print('--' * 10)
    for i, key in enumerate(LOCATIONS):
        print(f'{i+1}. {key} ')

    print('--' * 10)
    try:
        travel_choice = int(input('Куда путь держишь?: '))
        location = location_list[travel_choice - 1]
        local_enemy = LOCATIONS[location]['enemies']
        print (f'{location}. {LOCATIONS[location]["desc"]}')
        if not local_enemy:
            print('Нажми Enter чтобы уйти')
            input()
            return
        else:
            enemy_name  = random.choice(local_enemy)
            base_enemy = EMEMY_DATABASE[enemy_name]
            enemy = Enemy(base_enemy.name, base_enemy.hp, base_enemy.damage, base_enemy.reward_gold, base_enemy.reward_xp)
            print(f'На вас напал {enemy_name}  у него {enemy.hp} здоровья!')
            input('Нажмите Enter чтобы сразиться!')
            start_battle(hero,enemy)

    except  ValueError:
        print('Введи правильное число!')
    except IndexError:
        print('Такой локации не существует!')

