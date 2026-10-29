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
    'Гоблин': Enemy('Гоблин', 30, 3,6,5,5),
    'Орк': Enemy('Орк', 50, 8, 10, 8),
    'Волк': Enemy('Волк',30, 7, 8, 7 ),
    'Жаба-переросток': Enemy('Жаба-переросток', 55, 9, 15, 10),
    'Вампир': Enemy('Вампир', 40, 10, 20,10),
    'Зомби-шахтер': Enemy('Зомби-шахтер',60,6,10,9),
    'Крыса': Enemy('Крыса', 10, 3,3,1),
    'Огромный паук': Enemy('Огромный паук', 50, 10, 30, 20)
}
    
        