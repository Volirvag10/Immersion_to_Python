# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ —
# значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его
# строковое представление.

def dictionary(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[value] = key

    return result


temp = dictionary(a=4, b=5, c=7)
print(temp)
