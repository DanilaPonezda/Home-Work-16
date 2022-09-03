import time
from datetime import date
from colorama import Fore, Back, Style

datenow = date.today()
timenow = time.ctime()

menu = int(input(""" 
    Что вас интересует:
0 - Показать сегодняшнюю дату
1 - Узнать текущее время
2 - Записать текущюю дату и время в отдельный файл
"""))

if menu == 0:
    print(Fore . WHITE + 'Date: ' + Fore . BLUE + f'{datenow}')
elif menu == 1:
    print(Fore . WHITE + 'Time: ' + Fore. BLUE + f'{timenow}')
elif menu == 2:
    with open('datetime.txt', 'wt') as file:
        file.write(f'Date: {datenow} \nTime: {timenow}')