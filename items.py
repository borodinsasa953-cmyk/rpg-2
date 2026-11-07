
import random
from utils import ANSIColors
def effect_vampirism(hero, enemy, damage):
    heal_amount = max(1, damage // 3 )
    hero.heal(heal_amount)
    print(f'Эффект вампиризма! Вы восстановили {ANSIColors.GREEN}{heal_amount}{ANSIColors.RESET} HP')
    input()
def effect_double_hit(hero,enemy,damage):
    if random.randint(1,100) <= 30:
        print(f'Клинок наносит еще один удар и наносит дополнительно {ANSIColors.RED}{damage}{ANSIColors.RESET} урона!')
        input()
        enemy.take_damage(damage)
        if not enemy.is_alive():
            print(f'{enemy.name} падает замертво от двойного удара!')
            input()
ITEMS = {
    'Меч': {
        'name': 'Меч',
        'price': 40,
        'min_damage': 13,
        'max_damage': 20,
        'type': 'weapon',
        'desc': 'Обычный меч, увеличивает урон'
        

    },
    'Кольчуга': {
        'name': 'Кольчуга',
        'price': 50,
        'defence': 5,
        'type': 'armor',
        'desc': 'Легкая броня, защищает от ударов'
    },
    'Кинжал':{
        'name': 'Кинжал',
        'price': 65,
        'min_damage': 12,
        'max_damage': 17,
        'type': 'weapon',
        'desc': 'Быстрое и легкое оружие, может нанести два удара подряд.',
        'effect': effect_double_hit 

    },
    'Клинок Вампира':{
        'name':'Клинок Вампира',
        'price': 130,
        'min_damage': 18,
        'max_damage': 27,
        'type': 'weapon',
        'desc': 'Древнее и могущественное оружие. Исцеляет при нанесении урона.',
        'effect': effect_vampirism
    },
    'Зелье исцеления':{
        'name': 'Зелье исцеления',
        'price': 20,
        'heal': 20,
        'type': 'potion',
        'desc': 'Зелье исцеляющее 20 HP'
    }
    
}

list_items = list(ITEMS.keys())