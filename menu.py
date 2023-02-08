import bus
import driver
import route
import schedule
import os
import time
def cls():
    os.system('cls')

def main_menu():
    cls()
    print('*****Главное меню*****')
 
    print('1 - Автобусы\n'
          '2 - Водители\n'
          '3 - Маршруты\n'
          '4 - База назначений\n'
          '0 - Выход')


def Busbook():
    while True:
        main_menu()
        user_choice = input('Выберете необходимый пункт меню: ')

        match user_choice:
            case '1': bus.bus_menu()         
            case '2': driver.driver_menu()
            case '3': route.route_menu()
            case '4': schedule.schedule_menu()
            #case '5': ReplaceData(fileName)
            case '0': 
                print('До новых встреч!')
                break
            case _: 
                print('Будьте внимательнее!')
                time.sleep(1)   
