# 5. Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from Seminar_7_Task_4 import create_file


def generate_file(**kwargs) -> None:
	for extension, amount in kwargs.items():
		create_file(extension, count=amount)

if __name__ == '__main__':
	generate_file(bin=2, jpg=1, txt=3)
