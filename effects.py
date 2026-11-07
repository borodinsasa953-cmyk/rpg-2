from utils import ANSIColors
class StatusEffect:
    def __init__(self,name,duration, damage, is_heal = False):
        self.name = name
        self.duration = duration
        self.damage = damage
        self.is_heal = is_heal
    def tick(self, target):
        if self.is_heal == False:
            target.take_damage(self.damage)
            print(f'{target.name} получает {ANSIColors.RED}{self.damage} {ANSIColors.RESET} урона от эффекта {ANSIColors.PURPLE}{self.name}{ANSIColors.RESET}.')
        else:
            target.heal(self.damage)
            print(f'{target.name} исцеляет {ANSIColors.GREEN}{self.damage}{ANSIColors.RESET} HP от эффекта {ANSIColors.PURPLE}{self.name}{ANSIColors.RESET}.')

        self.duration -= 1

        if self.duration <= 0:
            print(f'Эффект {self.name} на {target.name} закончился.')
            return False
        return True
    def __repr__(self):
        return f'{self.name} (ходов: {self.duration})'

        
        

    
        