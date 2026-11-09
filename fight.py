from inventory import Inventory
from player import Player
from utils import give_name, clear_screen, ANSIColors, draw_hp_bar
from locations import LOCATIONS, location_list
from enemies import Enemy, EMEMY_DATABASE, berserk
from items import ITEMS
from effects import StatusEffect
import os
import random
import time
import copy
def is_boss_die(hero, enemy):
    if enemy.is_boss == True and not enemy.is_alive():
        clear_screen()
        time.sleep(0.5)
        hero.boss_die = True
        print('='* 40)
        print('ВЫ ПОБЕДИЛИ БОССА И СПАСЛИ МИР!')
        print('='* 40)
        clear_screen()
        input()
        clear_screen()
        print(f'Но тьма еще не ушла... Открыта новая локация: Бездна!')
        input()
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
        is_stunned = False
        is_enemy_stunned = False
        clear_screen()
        for effect in hero.effects[:]:
            if effect.is_stun:
                is_stunned = True
            is_alives = effect.tick(hero)
            if not is_alives:
                hero.effects.remove(effect)
        if not hero.is_alives():
            print('Вы не выдержали действия эффектов...')
            while True:
                clear_screen
                print('ВЫ ПОГИБЛИ...')
                print('1.Загрузить сохранение')
                print('2. Выйти')
                choice =  input('Выберите действие: ')
                if choice == '1':
                    from save_system import load_game
                    loaded_hero = load_game()
                    hero.__dict__.update(loaded_hero.__dict__)
                    print('Игра успешно загружена!')
                    input()
                    return
                elif choice == '2':
                    exit()
                else:
                    print('Неверный ввод!')
                    input()
        for effect in enemy.effects[:]:
            is_alive = effect.tick(enemy)
            if not is_alive:
                enemy.effects.remove(effect)
        more_damage = False
        print('=' * 40)
        print(f'Вы {ANSIColors.GREEN}({hero.name}){ANSIColors.RESET}: {draw_hp_bar(hero.hp, hero.max_hp)}')
        print(f'Враг {ANSIColors.RED}({enemy.name}){ANSIColors.RESET}: {draw_hp_bar(enemy.hp, enemy.max_hp)}')
        print(f'Ваши эффекты: {ANSIColors.GREEN}{hero.effects}{ANSIColors.RESET}')
        print(f'Эффекты врага: {ANSIColors.RED}{enemy.effects}{ANSIColors.RESET}')
        print('=' * 40)
        if is_stunned:
            print('Вы оглушены и не можете двигаться!')
            input()
        else:
            print(f'1. {ANSIColors.RED}Ударить{ANSIColors.RESET}' )
            print(f'2. {ANSIColors.PURPLE}Использовать предмет{ANSIColors.RESET}')
            print(f'3. {ANSIColors.YELLOW}Попытаться контратаковать{ANSIColors.RESET}')
            print(f'4. {ANSIColors.RED}Сильный удар{ANSIColors.RESET}')
            battle_choice = input('Твое действие: ')
            if battle_choice == '1':
                clear_screen()
                damage = random.randint(hero.min_damage, hero.max_damage)
                for effect in hero.effects[:]:
                    if effect.atk_mult != 1.0:
                        damage = int(damage * effect.atk_mult)
                        print(f'{ANSIColors.PURPLE}{effect.name}{ANSIColors.RESET} изменил ваш урон!')  
                        input()          
                clear_screen()
                time.sleep(0.5)
                print(f'Вы ударили врага на {ANSIColors.PURPLE}{damage}{ANSIColors.RESET} урона!')
                input()
                enemy.take_damage(damage)
                if hero.weapon_effect is not None:
                    hero.weapon_effect(hero,enemy,damage)
                if not enemy.is_alive():
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
                        get_reward(hero,enemy)
                        break
                    else:
                        continue
                else:
                    print('У вас не получилось!')
                    input()
            elif battle_choice == '4':
                if strong_attack():
                    clear_screen()
                    s_damage = int(random.randint(hero.min_damage, hero.max_damage) * 1.5)
                    for effect in hero.effects[:]:
                        if effect.atk.mult != 1.0:
                            s_damage = int(s_damage * effect.atk_mult)
                            print(f'{ANSIColors.PURPLE}{effect.name}{ANSIColors.RESET} изменил ваш урон!') 
                            input()
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
                                        
                        get_reward(hero,enemy)
                        break
                
        clear_screen()
        for effect in  enemy.effects:
            if effect.is_stun:
                is_enemy_stunned = True
        if is_enemy_stunned:
            print(f'{enemy.name} оглушен и не может атаковать!')
            input()
        else:  
            enemy.attack(hero,more_damage)
            if not hero.is_alives():
                while True:
                    clear_screen
                    print('ВЫ ПОГИБЛИ...')
                    print('1.Загрузить сохранение')
                    print('2. Выйти')
                    choice =  input('Выберите действие: ')
                    if choice == '1':
                        from save_system import load_game
                        loaded_hero = load_game()
                        hero.__dict__.update(loaded_hero.__dict__)
                        print('Игра успешно загружена!')
                        input()
                        return
                    elif choice == '2':
                        exit()
                    else:
                        print('Неверный ввод!')
                        input()
            
def start_boss_fight(hero, enemy):
    is_rage = False
    is_crazy = False
    print('=' * 40)
    print(f'⚔️   БОЙ:{ANSIColors.GREEN} {hero.name} {ANSIColors.RESET}  против {ANSIColors.RED}{enemy.name}{ANSIColors.RESET}')
    print('=' * 40)
    input()
    
    while hero.is_alives() and enemy.is_alive():

        clear_screen()
        for effect in enemy.effects[:]:
            is_alive = effect.tick(enemy)
            if not is_alive:
                enemy.effects.remove(effect)
        for effect in hero.effects[:]:
            is_alives = effect.tick(hero)
            if not is_alives:
                hero.effects.remove(effect)
        if not enemy.is_alive():
            print(f'{enemy.name} не выдержал действия эффекта...')
            input()
            is_boss_die(hero,enemy)
        if not hero.is_alives():
            while True:
                clear_screen
                print('ВЫ ПОГИБЛИ...')
                print('1.Загрузить сохранение')
                print('2. Выйти')
                choice =  input('Выберите действие: ')
                if choice == '1':
                    from save_system import load_game
                    loaded_hero = load_game()
                    hero.__dict__.update(loaded_hero.__dict__)
                    print('Игра успешно загружена!')
                    input()
                    return
                elif choice == '2':
                    exit()
                else:
                    print('Неверный ввод!')
                    input()
        if enemy.hp <= enemy.max_hp / 2 and is_rage == False:
            is_rage = True
            enemy.min_damage = int(enemy.min_damage * 1.5)
            enemy.max_damage = int(enemy.max_damage * 1.5)
            print(f'{ANSIColors.RED}{ANSIColors.BOLD}{enemy.name} впадает в ярость! Его глаза наливаются кровью. Урон увеличен!{ANSIColors.RESET}' )   
            input()
        if enemy.hp <= enemy.max_hp / 4 and is_crazy == False:
            is_crazy = True
            berserk2 = copy.deepcopy(berserk)
            enemy.min_damage = int(enemy.min_damage * 1.75)    
            enemy.max_damage = int(enemy.max_damage * 1.75) 
            enemy.effects.append(berserk2)
            print(f'{ANSIColors.BOLD}{ANSIColors.PURPLE} БОСС В БЕШЕНСТВЕ! ОН ВХОДИТ В РЕЖИМ БЕРСЕРКА! Удачи...{ANSIColors.RESET}')
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
            clear_screen()
            damage = random.randint(hero.min_damage, hero.max_damage)

            clear_screen()
            time.sleep(0.5)
            for effect in hero.effects[:]:
                if effect.atk.mult != 1.0:
                    damage = int(damage * effect.atk_mult)
                    print(f'{ANSIColors.PURPLE}{effect.name}{ANSIColors.RESET} изменил ваш урон!') 
                    input()
            print(f'Вы ударили врага на {ANSIColors.PURPLE}{damage}{ANSIColors.RESET} урона!')
            input()
            enemy.take_damage(damage)
            if hero.weapon_effect is not None:
                hero.weapon_effect(hero,enemy,damage)
            if not enemy.is_alive():
                is_boss_die(hero, enemy)
                get_reward(hero,enemy)
                break
        elif battle_choice == '2':
            clear_screen()
            has_potions = False
            for item in hero.inventory.items:
                if ITEMS[item]['type'] == 'potion':
                    has_potions = True
                    break
            if not has_potions:
                print('У вас нечего использовать!')
                input()
                continue
            else:
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
                    is_boss_die(hero,enemy)
                    get_reward(hero,enemy)
                    break
                else:
                    continue
            else:
                print('У вас не получилось!')
                input()
        elif battle_choice == '4':
            clear_screen()
            if strong_attack():
                s_damage = int(random.randint(hero.min_damage, hero.max_damage) * 1.5)
                enemy.take_damage(s_damage)
                for effect in hero.effects[:]:
                    if effect.atk.mult != 1.0:
                        s_damage = int(s_damage * effect.atk_mult)
                        print(f'{ANSIColors.PURPLE}{effect.name}{ANSIColors.RESET} изменил ваш урон!') 
                        input()
                print(f'Сокрушительный удар! Вы нанесли {ANSIColors.RED}{s_damage}{ANSIColors.RESET} урона!')
                if hero.weapon_effect is not None:
                    hero.weapon_effect(hero,enemy,s_damage)
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
        for effect in  enemy.effects:
            if effect.is_stun:
                is_enemy_stunned = True
        if is_enemy_stunned:
            print(f'{enemy.name} оглушен и не может атаковать!')
            input()
        else:

            enemy.attack(hero,more_damage)
            if not hero.is_alives():
                while True:
                    clear_screen
                    print('ВЫ ПОГИБЛИ...')
                    print('1.Загрузить сохранение')
                    print('2. Выйти')
                    choice =  input('Выберите действие: ')
                    if choice == '1':
                        from save_system import load_game
                        loaded_hero = load_game()
                        hero.__dict__.update(loaded_hero.__dict__)
                        print('Игра успешно загружена!')
                        input()
                        return
                    elif choice == '2':
                        exit()
                    else:
                        print('Неверный ввод!')
                        input()