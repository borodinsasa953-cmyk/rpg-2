from inventory import Inventory
from player import Player
import random
from utils import ANSIColors
import copy
from effects import  StatusEffect 

class Enemy:
    def __init__(self,name, hp, min_damage,max_damage,reward_gold, reward_xp,on_hit_effect = None, chance_of_effect = 30, is_boss = False):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.reward_gold = reward_gold
        self.reward_xp = reward_xp
        self.effects = []
        self.on_hit_effect = on_hit_effect
        self.chance_of_effect = chance_of_effect
        self.is_boss = is_boss
    def take_damage(self,amount):
        self.hp = max(0, self.hp - amount)
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
    def attack(self, target, more_damage):
        damage = random.randint(self.min_damage, self.max_damage)
        if more_damage == False:
            target.take_damage(damage)
            print(f'{self.name} атакует вас на {ANSIColors.RED}{damage}{ANSIColors.RESET} урона!')
            input()
        else:
            damage = int((damage * (random.randint(12,16) / 10)))
            print('Враг наносит больше урона!')
            print(f'{self.name} атакует вас на {ANSIColors.RED}{damage}{ANSIColors.RESET} урона!')
            input()
        if self.on_hit_effect is not  None:
            if random.randint(1, 100) <= self.chance_of_effect:
                new_effect = copy.deepcopy(self.on_hit_effect)
                target.effects.append(new_effect)
                print(f'{self.name} накладывает на  {target.name} эффект {new_effect.name}!')
                input()
    def is_alive(self):
        return self.hp> 0


poison_effect = StatusEffect('Яд жабы',3 ,5)
spider_poison_effect = StatusEffect('Яд паука', 5, 4)
burn_souls = StatusEffect('Пламя душ', 5, 5)
berserk = StatusEffect('Берсерк', 10, 15)
burn = StatusEffect('Горение', 3, 10)
vampirism = StatusEffect('Вампиризм', 5, 10,)


EMEMY_DATABASE = {
    'Гоблин': Enemy('Гоблин', 30, 3,6,5,10),
    'Орк': Enemy('Орк', 50, 4, 8, 10, 13),
    'Волк': Enemy('Волк',30, 4, 7, 8, 11 ),
    'Жаба-переросток': Enemy('Жаба-переросток', 55, 6, 10, 15, 18, on_hit_effect=poison_effect),
    'Вампир': Enemy('Вампир', 45, 7, 10, 20,18),
    'Зомби-шахтер': Enemy('Зомби-шахтер',60, 2, 6,10,16),
    'Крыса': Enemy('Крыса', 10,2,4,3,6),
    'Огромный паук': Enemy('Огромный паук', 50, 5, 10, 30, 25, on_hit_effect=spider_poison_effect, chance_of_effect=40),
    'Жнец душ': Enemy('Жнец душ', 200, 30, 45, 200, 200, on_hit_effect=burn_souls, chance_of_effect=25, is_boss = True ),
    'Херобрин': Enemy('Херобрин', 75,15,20,40,30 ),
    'Хрюшка-мясник': Enemy('Хрюшка-мясник', 70, 14, 19,41,25),
    'Чучело': Enemy('Чучело',60,10,15,35,25 ),
    'Медведь-мутант': Enemy('Медведь-мутант', 100, 20,35,80,50),
    'Зараженный сталкер': Enemy('Зараженный сталкер', 50, 11, 20, 20, 20),
    'Бес': Enemy('Бес', 150, 25, 40, 180, 150, on_hit_effect=burn,chance_of_effect=35 ),
    'Покровитель падших': Enemy('Покровитель падших', 300, 50, 65, 400, 250),
    'Высший вампир': Enemy('Высший вампир',400, 70, 80, 500, 400,on_hit_effect=vampirism, chance_of_effect= 40 )

}
    
        