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
        self.max_damage = 15
        self.kills = 0
        self.weapon = None
        self.armor = None
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
    def check_level_up(self):
        if self.xp > self.lvl * 50:
            self.xp -=  self.lvl *  50
            self.lvl += 1
            self.max_damage += 3
            self.min_damage += 3
            self.max_hp += 20
            self.hp = self.max_hp
            print(f'=== УРОВЕНЬ {self.lvl}! Здоровье и урон увеличены! ===')
    def equip_item(self, item_name):
        if item_name == 'Меч':
            if self.inventory.items.get('Меч', 0) > 0:
                self.weapon = 'Меч'
                print('Вы экипировали меч! ')
                input()
        elif item_name == 'Броня':
            if self.inventory.items.get('Броня', 0) > 0:
                self.armor = 'Броня'
                print('Вы экипировали броню!')
                input()
        else: 
            print('Такого предмета нет или его нельзя экипировать.')
        