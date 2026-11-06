import json
from player import Player
from items import ITEMS
def save_game(hero):
    data = {
        'name': hero.name,
        'clas': hero.clas,
        'hp': hero.hp,
        'xp':hero.xp,
        "lvl": hero.lvl,
        'gold': hero.gold,
        'max_hp': hero.max_hp,
        'min_damage': hero.min_damage,
        'max_damage': hero.max_damage,
        'kills': hero.kills,
        'weapon':hero.weapon,
        'armor':hero.armor,
        'inventory':hero.inventory.items,
        

    }
    with open('savegame.json','w',encoding='utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=4)
    print('Игра успешно сохранена!')
def load_game():
    try:
        with open('savegame.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        hero = Player(data['name'], data['clas'])

        hero.max_hp = data['max_hp']
        hero.clas = data['clas']
        hero.hp = data['hp']
        hero.gold = data['gold']
        hero.xp = data['xp']
        hero.lvl = data['lvl']
        hero.inventory.items = data['inventory']
        hero.min_damage = data['min_damage']
        hero.max_damage = data['max_damage']
        hero.kills = data['kills']
        hero.weapon = data['weapon']
        hero.armor = data['armor']
        if hero.armor is not  None:
            hero.armor_effect = ITEMS[hero.armor].get('effect', None)
        else:
            hero.weapon_effect = None
        if  hero.weapon is not None:
            hero.weapon_effect = ITEMS[hero.weapon].get('effect', None)
        else:
            hero.weapon_effect = None
        print('Игра успешно загружена!')
        return hero
    except  FileNotFoundError:
        print('Сохранений не найдено. Начинаю новую игру.')
        return  None
