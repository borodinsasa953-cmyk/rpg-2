
import random
from effects import StatusEffect
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
def effect_spikes(hero, enemy, damage):
    agressive_defence = damage // 4
    enemy.take_damage(agressive_defence)
    print(f'Ваша броня вернула {ANSIColors.PURPLE}{enemy.name}{ANSIColors.RESET} {ANSIColors.RED}{agressive_defence}{ANSIColors.RESET} урона!')
    input()
def effect_stunning(hero, enemy, damage):
    if random.randint(1,100) <= 30:
        stun = StatusEffect('Оглушение',1,is_stun=True)
        enemy.effects.append(stun)
        print('Оружие оглушило врага!')
        input()
def effect_poison(hero,enemy,damage):
    poison =  StatusEffect('Древний яд', 5, damage=8,atk_mult= 0.8)
    poison2 = StatusEffect('Яд', 3, damage= 3)
    choice_poison = random.randint(1,100)
    active_effects_names = [e.name for e in enemy.effects]
    if choice_poison <= 20 and 'Древний яд' not in active_effects_names:
        enemy.effects.append(poison)
        print(f'{ANSIColors.BOLD}Вы наложили на врага {ANSIColors.RED}Древний яд{ANSIColors.RESET}')
        input()
    elif 20<choice_poison<=100 and 'Яд' not in active_effects_names:
        enemy.effects.append(poison2)
        print(f'Вы наложили на врага яд!')
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
    'Кожаная куртка':{
        'name':'Кожаная куртка',
        'price': 30,
        'defence': 2,
        'type': 'armor',
        'desc': 'Защищает, но слабо. Дешево и сердито'


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
    'Шипастая кираса':{
        'name': 'Шипастая кираса',
        'price': 150,
        'defence': 10,
        'type': 'armor',
        'desc': 'Хорошая броня, атакующий вас сам получит часть урона!',
        'effect': effect_spikes

    },
    'Зелье исцеления':{
        'name': 'Зелье исцеления',
        'price': 20,
        'type': 'potion',
        'effect_type': 'heal',
        'power': 20,
        'desc': 'Зелье мгновенно исцеляющее 20 HP'
    },
    'Зелье регенерации':{
        'name': 'Зелье регенерации',
        'price': 35,
        'type': 'potion',
        'effect_type': 'regen',
        'power': 6,
        'duration': 5,
        'desc': 'Зелье накладывающее эффект регенерации исцеляющий 6 HP в течение 5 ходов'
    },
    'Зелье силы':{
        'name': 'Зелье силы',
        'price': 60,
        'type': 'potion',
        'effect_type': 'buff',
        'atk_mult': 1.5,
        'duration': 3,
        'desc': 'На короткое время увеличивает ваш урон'
    },
    'Дробитель':{
        'name':'Дробитель',
        'price': 250,
        'type': 'weapon',
        'min_damage': 30,
        'max_damage': 45,
        'desc': 'Мощное и тяжелое оружие, его удар может оглушить врага!',
        'effect': effect_stunning,
        'requries_boss': True
    },
    'Проклятое жало древних':{
        'name': 'Проклятое жало древних',
        'price': 550,
        'type': 'weapon',
        'min_damage': 55,
        'max_damage': 67,
       'desc':'Невероятно сильное оружие, способное отравлять врагов древним ядом...',
       'effect': effect_poison,
       'requries_boss': True
    }
}

list_items = list(ITEMS.keys())