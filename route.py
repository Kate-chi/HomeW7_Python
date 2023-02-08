import os
import time

fileName = 'route.txt'

def cls():
    os.system('cls')
cls()

def route_menu():
    cls()
    while True:
        print('*****Меню маршрутов*****')
 
        print('1 - Список маршрутов\n'
              '2 - Добавить новый маршрут\n'
              '3 - Удалить маршрут\n'
              '0 - Выход')
        user_choice = input('Выберете необходимый пункт меню: ')
        match user_choice:
            case '1':
                readFile(fileName)
            case '2':
                writeFile(fileName)
            case '3':
                Delete(fileName)
            case '0': 
                return
            case _: 
                print('Будьте внимательнее!')
                time.sleep(1) 


def writeFile (file_name):
    cls()
    print('*****Добавление нового маршрута*****')

    while True:
        with open (file_name, 'a+', encoding = 'utf-8') as data:
            route_id = input('ID маршрута: ')
            start_route = input('Начало маршрута: ')
            end_route = input('Конец маршрута: ')

            data.writelines(f'\n{route_id} {start_route} - {end_route}')
            choice = input('Нажмите Enter чтобы добавить новый маршрут\nВведите 0 для выхода\n')
            if choice == '0': 
                return 

def readFile (file_name):
    cls()
    print('*****Список маршрутов*****')
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
            
        for i in line:
            i = line.index(i)
            print(f'{i + 1}. {line[i].strip()}')
        choice = input('\nНажмите 0 для выхода\n')
        if choice == '0': 
            return
        
def Delete(file_name):
    cls()
    print('*****Удаление маршрута*****\n')             
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
        
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        
        deleted_str = int(input('Введите порядковый номер маршрута, который хотите удалить: '))
        del line[deleted_str - 1]
        
        with open (file_name, 'w', encoding = 'utf-8') as data:
            for i in line:
                data.write(i)
        choice = input('\nНажмите Enter, чтобы продолжить удаление маршрутов\nВведите 0 для выхода\n')
        if choice == '0': 
            return  