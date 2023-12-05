# 1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Вариант решения 1.

def parse_path(text: str) -> tuple:
    full_path = text
    file_name = full_path.split('\\')[-1].split('.')[0]
    file_extension = full_path.split('\\')[-1].split('.')[1]
    dir_name = '/'.join(full_path.split('\\')[0:-1])

    return dir_name, file_name, file_extension


my_file = parse_path('C:\Windows\Cursors\File.doc')
print(my_file)


# Вариант решения 2.

def parse_path(text: str) -> tuple:
    full_path = text
    *dir_name, full_file_name = full_path.split('\\')
    file_name = full_file_name.split('.')[0]
    file_extension = full_file_name.split('.')[1]
    full_dir_name = '/'.join(dir_name)
    return full_dir_name, file_name, file_extension


my_file = parse_path('C:\Windows\Cursors\File.doc')
print(my_file)