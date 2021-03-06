# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import hw05_easy
import os

def show_menu():
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')

answer = ''
while answer != 'q':
    show_menu()
    cur_path = os.getcwd()
    print(cur_path + '>')
    answer = input("Выберите действие (1-4) q - выход : ")
    if answer == '1':
        folder_path = input("Укажите папку для перехода : ")
        os.chdir(folder_path)
    if answer == '2':
        dirs = os.scandir(path=".")
        for dir in dirs:
            print(dir.name)
    if answer == '3':
        folder_name = input("Укажите папку для удаления : ")
        hw05_easy.del_folder(folder_name)
    if answer == '4':
        folder_name = input("Укажите папку для создания : ")
        hw05_easy.make_folder(folder_name)
