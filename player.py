from inventory import Inventory
class Player:
    def __init__(self, name):
        self.name  = name
        self.max_hp = 100
        self.hp = 100
        self.gold = 0
        self.xp = 0
        self.lvl = 1 
        self.inventory = Inventory()
        self.min_damage = 10
        self.max_damage = 20
        self.kills = 0
    def take_damage (self, amount):
        self.hp  = max(0, self.hp - amount)
    def heal (self, amount):
        self.hp = min (self.max_hp, self.hp + amount)
    def show_stats(self):
        print('ХАРАКТЕРИСТИКИ:')
        print('=======================')
        print(f'Имя: {self.name}')
        print('=======================')
        print(f'Здоровье: {self.hp}')
        print(f'Золото: {self.gold}')
        print('=======================')
        print(f'Уровень: {self.lvl}')
        print(f'Опыт: {self.xp} / 50')
        print(f'Убийства: {self.kills}')
        print('=======================')
    def is_alives(self):
        return self.hp > 0
