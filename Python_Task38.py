# Урок 8. Работа с файлами
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

import os
os.chdir(r'C:\Users\DMM\Desktop\Programm_Python\Python_Praktikal_Task_Seminar8')
# Смена текущей директории к месту где лежит наш справочник
#print(os.getcwd())


def menu(): 
    print('________________________________') 
    print('Вам доступны следующие действия:') 
    print('1 - просмотр справочника') 
    print('2 - добавление записи') 
    print('3 - поиск') 
    print('4 - удаление по id') 
    print('0 - выход') 
    print('________________________________') 

def read_guide():# функция для чтения данных из справочника
    filename = 'guide.txt'
    data = open(filename, 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()
    
    
def add_record_guide(): # функция для добавление данных в справочник
    filename = 'guide.txt'
    id = input('Введите id новой записи: ') 
    name = input('Введите ФИО новой записи: ') 
    tel = input('Введите новый номер телефона: ') 
    new_data = id +'   ' + name + '   ' + tel # id, ФИО и  номер телефона разделяем трмя пробелами
    print(f'Вы хотите добавить запись вот такого вида: {new_data}')
    my_choice_add_record = int(input('Если все верно введите 1, иначе введите 0 :'))
    if my_choice_add_record == 1:
        data = open(filename, 'a', encoding='utf-8') 
        data.writelines('\n' + new_data) 
        data.close()
    else:
        return 

def search_guide() : # функция для поиска в справочнике
    whom = input('Введите строку для поиска: ') 
    filename = 'guide.txt'
    data = open(filename, 'r', encoding='utf-8')
    for line in data:
        if whom in line:
            print(line)
    data.close()

def delete_record_guide(): # функция для удаления по id в справочнике
    id = input('Введите id для удаления: ') + '   '
    filename = 'guide.txt'
    data = open(filename, 'r', encoding='utf-8')
    
    new_guide = [] 
    for elem in data: 
        if id not in elem: 
            new_guide.append(elem) 
    
    data.close()
    data = open(filename, 'w', encoding='utf-8')
    for line in new_guide:
        data.writelines(line)

    data.close()

# Основная часть программы
while menu != 0:
    menu()    
    my_choice = int(input('Сделайте выбор:'))
    if my_choice == 0:
        print('До новых встреч')
        exit()
    elif my_choice == 1 : 
        read_guide()
    elif my_choice == 2 :
        add_record_guide()
    elif my_choice == 3 :
        search_guide()
    elif my_choice == 4 :
        delete_record_guide()       

