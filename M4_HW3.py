from colorama import Fore, Back, Style
from pathlib import Path
import sys

"""
Вимоги до завдання:
Створіть віртуальне оточення Python для ізоляції залежностей проєкту.
Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
Використання бібліотеки colorama для реалізації кольорового виведення.
Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.

Рекомендації для виконання:
Спочатку встановіть бібліотеку colorama. Для цього створіть та активуйте віртуальне оточення Python, а потім встановіть пакет за допомогою pip.
Використовуйте модуль sys для отримання шляху до директорії як аргументу командного рядка.
Для роботи з файловою системою використовуйте модуль pathlib.
Забезпечте належне форматування виводу, використовуючи функції colorama.
"""
def get_dir_info(input_path: Path):
    symbol = '-'
    if input_path.exists():                 # checking path on exsting
        all_path = input_path.glob('**/*')  #getting recoursiv of pathes
        for path in all_path:
            if path.is_dir():               #setting up a style for dirs
                print(Fore.LIGHTRED_EX + f"{symbol*len(path.parts)}{path.parts[len(path.parts)-2]}\\{path.parts[len(path.parts)-1]}")

            if path.is_file():              #setting up a style for files
                print(Fore.BLUE + f"{symbol*len(path.parts)}{path.parts[len(path.parts)-2]}\\{path.name}")
    else:
        print(f"Entered path {input_path} is not exsist")

def main():
    if len(sys.argv)<2:           # check weather we have arg in command prompt
        path_info = ''
    else: 
        path_info = sys.argv[1]   #"D:\\Ihor\\lytvinenko.i GDrive\\AI coding\\GoIT_Python+DataScience\\HomeWorks\\Module3\\"
    path = Path(path_info)
    get_dir_info(path)
    print(Style.RESET_ALL) #reset all styles

if __name__ == "__main__":
    main()