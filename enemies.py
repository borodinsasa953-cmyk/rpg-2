from inventory import Inventory
from player import Player

class Enemy:
    def __init__(self,name, hp, damage,reward_gold, reward_xp ):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
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
           
baba = Player('baba')
goblin = Enemy('Гоблин', 50,10,15,5)
goblin.attack(baba)
baba.show_stats()
    
        