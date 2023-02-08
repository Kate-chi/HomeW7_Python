import os
import time




fileName = 'schedule.txt'

def cls():
    os.system('cls')
cls()

def schedule_menu():
    cls()
    while True:
        print('*****Назначения автопарка*****')
 
        print('1 - Показать все данные\n'
              '0 - Выход')
        user_choice = input('Выберете необходимый пункт меню: ')
        match user_choice:
            case '1':
                readFile(fileName)
            case '0': 
                return
            case _: 
                print('Будьте внимательнее!')
                time.sleep(1) 

def readFile (file_name):
    cls()
    print('*****Список автобусов*****')
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
            
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        choice = input('\nНажмите 0 для выхода\n')
        if choice == '0': 
            return




        