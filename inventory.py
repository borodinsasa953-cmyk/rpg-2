class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self,item_name, qty = 1):
        if item_name in self.items:
            self.items[item_name] += qty
        else:
            self.items[item_name] = qty
        return self.items
    def show_items(self):
        print(self.items)
    def remove_item(self,item_name,qty = 1):
        if qty > 0:
            if item_name in self.items:
                if self.items[item_name] < qty:
                    print('В инвентаре нет столько предметов!')
                else:
                    self.items[item_name] -= qty
                    if self.items[item_name] == 0:
                        del self.items[item_name]
            
            else:
                print('Такого предмета нет в инвентаре!')
        else:
            print('Введи нормальное число!')
        return self.items
inventory = Inventory()
