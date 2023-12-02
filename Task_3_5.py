# 3. Создайте функцию генератор чисел Фибоначчи.

def gen_fib() -> list[int]:
    num_1, num_2 = 0, 1
    num = int(input('Введите порядковый номер элемента последовательности Фибоначчи: '))
    for i in range(num):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


data = list(gen_fib())
print(data)