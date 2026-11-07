
import os
import unicodedata
import random

def give_name():
    player_name = input('Введи свое имя странник: ')
    
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
    BOLD = '\033[1m'
def draw_hp_bar(hp, hp_max):
    if hp_max == 0:
        return '♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ 0/0'
    count = int((hp / hp_max) * 10)
    bar = ' ❤ '* count + ' ♡ ' * (10 - count)
    return f'[{bar}]  {hp} / {hp_max}' 
prt = ("""
\033[93m╔══════════════════════════════════════════════════════════════╗
\033[93m║\033[97m                                                              \033[93m║
\033[93m║\033[96m              Добро пожаловать в мир, странник!               \033[93m║
\033[93m║\033[97m                                                              \033[93m║
\033[93m║\033[97m                    Как тебя зовут?                           \033[93m║
\033[93m║\033[97m                                                              \033[93m║
\033[93m╚══════════════════════════════════════════════════════════════╝\033[0m
""")
import unicodedata


def _char_width(ch: str) -> int:
    """Возвращает визуальную ширину одного символа (0, 1 или 2)."""
    if unicodedata.combining(ch):
        return 0
    cat = unicodedata.category(ch)
    # Управляющие и форматирующие символы — нулевой ширины
    if cat in ("Mn", "Me", "Cf", "Cc"):
        return 0
    # Восточно-азиатские широкие символы и эмодзи
    if unicodedata.east_asian_width(ch) in ("W", "F"):
        return 2
    # Эмодзи-диапазоны (широкие)
    cp = ord(ch)
    if (0x1F300 <= cp <= 0x1FAFF or
        0x2600  <= cp <= 0x27BF  or
        0x1F000 <= cp <= 0x1F02F):
        return 2
    return 1


def _disp_len(s: str) -> int:
    """Визуальная длина строки с учётом широких символов."""
    return sum(_char_width(ch) for ch in s)


def _pad(s: str, width: int, align: str = "left", fill: str = " ") -> str:
    """Дополняет строку до нужной визуальной ширины."""
    diff = width - _disp_len(s)
    if diff <= 0:
        return s
    if align == "left":
        return s + fill * diff
    if align == "right":
        return fill * diff + s
    # center
    left = diff // 2
    return fill * left + s + fill * (diff - left)


def frame_text(text: str, style: str = "double", padding: int = 1,
               align: str = "center", min_width: int = 0) -> str:
    """
    Оборачивает текст в красивую рамку (без внешних зависимостей).
    Корректно работает с кириллицей, эмодзи и CJK-символами.

    :param text:      Текст (может быть многострочным).
    :param style:     'single', 'double', 'rounded', 'bold',
                      'ascii', 'stars', 'hash', 'dashed'.
    :param padding:   Отступ внутри рамки (пробелы).
    :param align:     'left', 'center', 'right'.
    :param min_width: Минимальная ширина внутренней части.
    """
    styles = {
        "single":  ("┌", "┐", "└", "┘", "─", "│"),
        "double":  ("╔", "╗", "╚", "╝", "═", "║"),
        "rounded": ("╭", "╮", "╰", "╯", "─", "│"),
        "bold":    ("┏", "┓", "┗", "┛", "━", "┃"),
        "ascii":   ("+", "+", "+", "+", "-", "|"),
        "stars":   ("*", "*", "*", "*", "*", "*"),
        "hash":    ("#", "#", "#", "#", "#", "#"),
        "dashed":  ("┌", "┐", "└", "┘", "╌", "╎"),
    }
    tl, tr, bl, br, h, v = styles.get(style, styles["double"])

    lines = text.splitlines() or [""]
    inner_width = max([_disp_len(line) for line in lines] + [min_width])
    total_width = inner_width + padding * 2

    top    = tl + h * total_width + tr
    bottom = bl + h * total_width + br
    empty  = v + " " * total_width + v

    result = [top]
    for _ in range(padding):
        result.append(empty)
    for line in lines:
        content = _pad(line, inner_width, align)
        result.append(v + " " * padding + content + " " * padding + v)
    for _ in range(padding):
        result.append(empty)
    result.append(bottom)

    return "\n".join(result)
if __name__ == "__main__":
    print(frame_text("Привет, мир!"))
    print()
    print(frame_text("Python 🐍", style="rounded", padding=2))
    print()
    print(frame_text("Многострочный\nтекст в рамке\nс выравниванием",
                     style="double", align="left"))
    print()
    print(frame_text("汉字 테스트 🎉", style="bold"))
    print()
    print(frame_text("ASCII", style="ascii"))