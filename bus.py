import os
import time

fileName = 'bus.txt'

def cls():
    os.system('cls')
cls()

def bus_menu():
    cls()
    while True:
        print('*****Автобусное меню*****')
 
        print('1 - Список автобусов\n'
              '2 - Добавить новый автобус\n'
              '3 - Удалить автобус\n'
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
    print('*****Добавление нового автобуса*****')

    while True:
        with open (file_name, 'a+', encoding = 'utf-8') as data:
            bus_id = input('ID автобуса: ')
            bus_number = input('Номер автобуса: ')

            data.writelines(f'\n{bus_id} {bus_number}')
            choice = input('Нажмите Enter чтобы добавить новый автобус\nВведите 0 для выхода\n')
            if choice == '0': 
                return 

def readFile (file_name):
    cls()
    print('*****Список автобусов*****')
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
    print('*****Удаление автобуса*****\n')             
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
        
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        
        deleted_str = int(input('Введите порядковый номер автобуса, который хотите удалить: '))
        del line[deleted_str - 1]
        
        with open (file_name, 'w', encoding = 'utf-8') as data:
            for i in line:
                data.write(i)
        choice = input('\nНажмите Enter, чтобы продолжить удаление автобусов\nВведите 0 для выхода\n')
        if choice == '0': 
            return   