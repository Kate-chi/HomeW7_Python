import os
import time

fileName = 'driver.txt'

def cls():
    os.system('cls')
cls()

def driver_menu():
    cls()
    while True:
        print('*****Водительское меню*****')
 
        print('1 - Список водителей\n'
              '2 - Добавить нового водителя\n'
              '3 - Удалить водителя\n'
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
    print('*****Добавление нового водителя*****')

    while True:
        with open (file_name, 'a+', encoding = 'utf-8') as data:
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            patronymic = input('Отчество: ')

            data.writelines(f'\n{last_name} {first_name} {patronymic}')
            choice = input('Нажмите Enter чтобы добавить нового водителя\nВведите 0 для выхода\n')
            if choice == '0': 
                return 

def readFile (file_name):
    cls()
    print('*****Список водителей*****')
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
    print('*****Удаление водителя*****\n')             
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
        
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        
        deleted_str = int(input('Введите порядковый номер водителя, который хотите удалить: '))
        del line[deleted_str - 1]
        
        with open (file_name, 'w', encoding = 'utf-8') as data:
            for i in line:
                data.write(i)
        choice = input('\nНажмите Enter, чтобы продолжить удаление водителей\nВведите 0 для выхода\n')
        if choice == '0': 
            return  