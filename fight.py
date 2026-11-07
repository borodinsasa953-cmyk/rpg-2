from inventory import Inventory
from player import Player
from utils import give_name, clear_screen, ANSIColors, draw_hp_bar
from locations import LOCATIONS, location_list
from enemies import Enemy, EMEMY_DATABASE
from items import ITEMS
import os
import random
import time
def is_boss_die(hero, enemy):
    if enemy.name == 'Жнец душ':
        clear_screen()
        time.sleep(0.5)
        print('='* 40)
        print('ВЫ ПОБЕДИЛИ БОССА И СПАСЛИ МИР!')
        print('='* 40)
        exit()
def get_reward(hero,enemy):
    clear_screen()
    time.sleep(1)
    print(f'Вы победили {enemy.name}! ')
    hero.gold += enemy.reward_gold
    hero.xp += enemy.reward_xp
    hero.kills += 1
    print(f'Вы получили {enemy.reward_gold} золота и {enemy.reward_xp} опыта!')
    hero.check_level_up()
    input()
def contr_attack():
    attack_roll = random.randint(1,100)
    if 1 <= attack_roll <= 30:
        return True
    else:
        return False
def strong_attack():
    s_attack_roll = random.randint(1,100)
    return 1 <= s_attack_roll <= 70
def start_battle(hero, enemy):
    clear_screen()
    print('=' * 40)
    print(f'⚔️   БОЙ:{ANSIColors.GREEN} {hero.name} {ANSIColors.RESET}  против {ANSIColors.RED}{enemy.name}{ANSIColors.RESET}')
    print('=' * 40)
    input()
    
    while hero.is_alives() and enemy.is_alive():

        clear_screen()
        for effect in hero.effects[:]:
            is_alives = effect.tick(hero)
            if not is_alives:
                hero.effects.remove(effect)
        if not hero.is_alives():
            print('Вы не выдержали действия эффектов...')
            input('Нажмите Enter...')
            exit()
                
        more_damage = False
        print('=' * 40)
        print(f'Вы {ANSIColors.GREEN}({hero.name}){ANSIColors.RESET}: {draw_hp_bar(hero.hp, hero.max_hp)}')
        print(f'Враг {ANSIColors.RED}({enemy.name}){ANSIColors.RESET}: {draw_hp_bar(enemy.hp, enemy.max_hp)}')
        print(f'Ваши эффекты: {ANSIColors.GREEN}{hero.effects}{ANSIColors.RESET}')
        print(f'Эффекты врага: {ANSIColors.RED}{enemy.effects}{ANSIColors.RESET}')
        print('=' * 40)
        
        
        print(f'1. {ANSIColors.RED}Ударить{ANSIColors.RESET}' )
        print(f'2. {ANSIColors.PURPLE}Использовать предмет{ANSIColors.RESET}')
        print(f'3. {ANSIColors.YELLOW}Попытаться контратаковать{ANSIColors.RESET}')
        print(f'4. {ANSIColors.RED}Сильный удар{ANSIColors.RESET}')
        battle_choice = input('Твое действие: ')
        if battle_choice == '1':
            damage = random.randint(hero.min_damage, hero.max_damage)
            clear_screen()
            time.sleep(0.5)
            print(f'Вы ударили врага на {ANSIColors.PURPLE}{damage}{ANSIColors.RESET} урона!')
            input()
            enemy.take_damage(damage)
            if hero.weapon_effect is not None:
                hero.weapon_effect(hero,enemy,damage)
            if not enemy.is_alive():

                if enemy.name == 'Жнец душ':

                    clear_screen()
                    time.sleep(0.5)
                    print('='* 40)
                    print('ВЫ ПОБЕДИЛИ БОССА И СПАСЛИ МИР!')
                    print('='* 40)
                    exit()
                else:
                    get_reward(hero,enemy)
                    break
        elif battle_choice == '2':
            clear_screen()
            item_used = hero.use_item()
            if  not item_used:
                continue
            
            
           
        elif battle_choice == '3':
            if contr_attack() == True:
                edamage = random.randint(enemy.min_damage, enemy.max_damage)
                enemy.take_damage(edamage)
                print(f'Вы успешно контратаковали! Враг ударил сам себя на {ANSIColors.RED}{edamage}{ANSIColors.RESET} урона!')
                input()
                if not enemy.is_alive():
                    is_boss_die()
                    
                    get_reward(hero,enemy)
                    break
                else:
                    continue
            else:
                print('У вас не получилось!')
                input()
        elif battle_choice == '4':
            if strong_attack():
                s_damage = int(random.randint(hero.min_damage, hero.max_damage) * 1.5)
                if hero.weapon ==  'Меч':
                    s_damage += 5
                enemy.take_damage(s_damage)
                print(f'Сокрушительный удар! Вы нанесли {ANSIColors.RED}{s_damage}{ANSIColors.RESET} урона!')
                input()
            else:
                more_damage = True
                print('Вы промахнулись!')
                input()
                if not enemy.is_alive():
                    is_boss_die(hero, enemy)
                                    
                    get_reward(hero,enemy)
                    break
                
        clear_screen()
        enemy.attack(hero,more_damage)
        if not hero.is_alives():
            clear_screen()
            print('GAME OVER')
            input()
            break
            exit()