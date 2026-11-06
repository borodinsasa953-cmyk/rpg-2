
import random
def effect_vampirism(hero, enemy, damage):
    heal_amount = max(1, damage // 2 )
    hero.heal(heal_amount)
    print(f'Эффект вампиризма!  Вы восстановили {heal_amount} HP')
def effect_double_hit(hero,enemy,damage):
    if random.randint(1,100) <= 30:
        print(f'Клинок наносит еще один удар!')
        enemy.take_damage(damage)
        if not enemy.is_alive():
            print(f'{enemy.name} падает замертво от двойного удара!')
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
    }
}

list_items = list(ITEMS.keys())