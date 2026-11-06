from inventory import Inventory
from utils import ANSIColors
from items import ITEMS, effect_vampirism, effect_double_hit
def take_class():
    print('--' * 30)
    print(f'{ANSIColors.RED}ВЫБОР КЛАССА:{ANSIColors.RESET}')
    print(f'{ANSIColors.GREEN}~-{ANSIColors.RESET}' * 30)
    for i, key in enumerate(PLAYER_CLASS):
        desc =  PLAYER_CLASS[key]['desc']
        print(f'{i + 1}. {ANSIColors.RED}{key}{ANSIColors.RESET}  {ANSIColors.BLUE}({desc}) {ANSIColors.RESET}')
    print('0. Выйти.')
    print(f'{ANSIColors.GREEN}~-{ANSIColors.RESET}' * 30)
    try:
        class_choice = int(input('Выбери свой класс: '))
        if class_choice == 0:
            exit()
        clas = list_class[class_choice - 1]
        print(f'Отлично! Теперь ваш класс - {clas}')
        return clas
    except ValueError:
        print('Введи правильное число!')
    except KeyboardInterrupt:
        print('Неверный ввод')
    except IndexError:
        print('Нет такого варианта!')

class Player:
    def __init__(self, name, clas):
        self.name  = name
        self.clas = clas
        self.max_hp = PLAYER_CLASS[clas]['hp']
        self.hp = PLAYER_CLASS[clas]['hp']
        self.gold = 0
        self.xp = 0
        self.lvl = 1 
        self.inventory = Inventory()
        self.min_damage = PLAYER_CLASS[clas]['min_damage']
        self.max_damage = PLAYER_CLASS[clas]['max_damage']
        self.kills = 0
        self.weapon = None
        self.armor = None
        self.weapon_effect = None
        self.defence = 0
        self.armor_effect = None
    def take_damage (self, amount):
        self.hp  = max(0, self.hp - amount)
    def heal (self, amount):
        self.hp = min (self.max_hp, self.hp + amount)
    def show_stats(self):
        print('ХАРАКТЕРИСТИКИ:')
        print('=======================')
        print(f'{ANSIColors.PURPLE}Имя: {self.name}{ANSIColors.RESET}')
        print(f'{ANSIColors.RED}Класс: {ANSIColors.RESET}{ANSIColors.PURPLE} {self.clas} {ANSIColors.RESET}')
        print('=======================')
        print(f'{ANSIColors.RED}Здоровье: {self.hp}{ANSIColors.RESET}')
        print(f'{ANSIColors.YELLOW}Золото: {self.gold}{ANSIColors.RESET}')
        print('=======================')
        print(f'{ANSIColors.GREEN}Уровень: {self.lvl}{ANSIColors.RESET}')
        print(f'{ANSIColors.CYAN}Опыт: {self.xp} / 50 {ANSIColors.RESET}')
        print(f'Убийства: {self.kills}')
        print('=======================')
        print('ЭКИПИРОВКА:')
        print(f'Оружие: {self.weapon}')
        print(f'Броня: {self.armor}')
        if self.weapon_effect or self.armor_effect:
            print('Эффект: Активен')
        else:
            print('Эффект: Неактивен')
        print(f'======================')
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
        if self.inventory.items.get(item_name, 0) <= 0:
            print('У вас нет такого предмета!')
            return
        if item_name in ITEMS:
            item_data = ITEMS[item_name]

            if item_data['type'] == 'weapon':
                self.weapon = item_name
                self.min_damage = item_data['min_damage']
                self.max_damage = item_data['max_damage']
                self.weapon_effect = item_data.get('effect', None)
                print(f'Вы экипировали {item_name}! Урон: {ANSIColors.RED}{self.min_damage} - {self.max_damage}{ANSIColors.RESET}')
                input()
            elif item_data['type'] == 'armor':
                self.armor = item_name
                self.defence = item_data['defence']
                self.armor_effect = item_data.get('effect', None)
                print(f'Вы экипировали {item_name}! Защита: {ANSIColors.CYAN}{self.defence}{ANSIColors.RESET}')
                input()
        else:
            print('Этот предмет нельзя экипировать')
            input()
        
PLAYER_CLASS = {
    'Маг' : {
        'name': 'Маг',
        'hp': 75,
        'min_damage': 13,
        'max_damage': 20,
        'desc': 'Умирает быстро. Но убивает еще быстрее.'
    },
    'Рыцарь': {
        'name': 'Рыцарь',
        'hp': 120,
        'min_damage': 7,
        'max_damage': 12,
        'desc': 'Крепкий орешек. Бьет слабовато.'

    },
    'Разбойник': {
        'name': 'Разбойник',
        'hp' : 100,
        'min_damage': 10,
        'max_damage': 15,
        'desc': 'Привык брать от жизни всё. Средний боец'

    }
}
list_class = list(PLAYER_CLASS.keys())

        