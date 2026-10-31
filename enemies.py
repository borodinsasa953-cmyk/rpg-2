from inventory import Inventory
from player import Player

class Enemy:
    def __init__(self,name, hp, min_damage,max_damage,reward_gold, reward_xp ):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.reward_gold = reward_gold
        self.reward_xp = reward_xp
    def take_damage(self,amount):
        self.hp = max(0, self.hp - amount)
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
    def attack(self, target):
        target.take_damage(self.damage)
        print(f'{self.name} бьет {target.name} и наносит {self.damage} урона!')
    def is_alive(self):
        return self.hp> 0
           
EMEMY_DATABASE = {
    'Гоблин': Enemy('Гоблин', 30, 3,6,5,10),
    'Орк': Enemy('Орк', 50, 4, 8, 10, 13),
    'Волк': Enemy('Волк',30, 4, 7, 8, 11 ),
    'Жаба-переросток': Enemy('Жаба-переросток', 55, 6, 10, 15, 18),
    'Вампир': Enemy('Вампир', 45, 7, 10, 20,18),
    'Зомби-шахтер': Enemy('Зомби-шахтер',60, 2, 6,10,16),
    'Крыса': Enemy('Крыса', 10,2,4,3,6),
    'Огромный паук': Enemy('Огромный паук', 50, 5, 10, 30, 25),
    'Жнец душ': Enemy('Жнец душ', 200, 30, 45, 200, 200 )
}
    
        