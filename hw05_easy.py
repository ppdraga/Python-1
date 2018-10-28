# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# import os

def make_folder(folder_name):
    import os
    dir_path = os.path.join(os.getcwd(), folder_name)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('директория {} уже существует'.format(dir_path))

def del_folder(folder_name):
    import os
    dir_path = os.path.join(os.getcwd(), folder_name)
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('директория {} не найдена'.format(dir_path))


if __name__ == "__main__":

    idx = 1
    while idx < 10:
        dir_name = 'dir_' + str(idx)
        make_folder(dir_name)
        # try:
        #     os.mkdir(dir_name)
        # except FileExistsError:
        #     print('директория {} уже существует'.format(dir_name))
        idx += 1

    idx = 1
    while idx < 10:
        dir_name = 'dir_' + str(idx)
        del_folder(dir_name)
        # from os import rmdir
        # try:
        #     rmdir(dir_name)
        # except FileNotFoundError:
        #     print('директория {} не найдена'.format(dir_name))
        idx += 1


    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.
    from os import scandir
    dirs = scandir(path=".")
    for dir in dirs:
        if dir.is_dir():
            print(dir.name)

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    import sys
    import shutil
    src = sys.argv[0]
    dst = src[:-3] + '_copy.py'

    shutil.copyfile(src, dst)