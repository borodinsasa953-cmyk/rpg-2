
import os
import random

def give_name():
    player_name = input()
    
    return player_name
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class ANSIColors:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
def draw_hp_bar(hp, hp_max):
    if hp_max == 0:
        return '♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 0/0'
    count = int((hp / hp_max) * 10)
    bar = ' ❤ '* count + ' ♡ ' * (10 - count)
    return f'[{bar}]  {hp} / {hp_max}' 
