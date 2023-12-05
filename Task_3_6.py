# 3. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различныe случайные варианты и выведите 4 успешных расстановки.


import random
from random import randint
from Task_2_6 import validate_queens


# Вариант 1

def queens_rnd_x_y():
    queens = []
    count = 1
    for _ in range(1, 9):
        queens.append([count, randint(1, 8)])
        count += 1
    return queens


print(queens_rnd_x_y())
print(validate_queens(queens_rnd_x_y()))


# Вариант 2

def queens_rnd_x_y():
    x = [i for i in range(1, 9)]
    y = [random.randrange(1, 9) for i in range(1, 9)]
    res = []
    for x, y in zip(x, y):
        res.append([x, y])

    for el in res:
        random.shuffle(res)

    return res


print(queens_rnd_x_y())
print(validate_queens(queens_rnd_x_y()))

# cor_res = []
# while True:
#     call_func = queens_rnd_x_y()
#     if validate_queens(call_func) is True:
#         cor_res.append(call_func)
#     if len(cor_res) == 4:
#         break
#
# print(cor_res)
#
# Логика программы:
# 1) Создаем пустой список, который будет хранить все списки с успешными расстановками;
# 2) Запускаем бесконечный цикл, в котором:
# 2.1) Вызываем функцию генерации случайных расстановок;
# 2.2) Проверяем, выдает ли функция проверки вариантов расстановок True или False;
# 2.3) Если получаем True, добавляем в список с успешными расстановками;
# 3) Если количество элементов в результирующем списке равно 4, цикл прекращаем.
