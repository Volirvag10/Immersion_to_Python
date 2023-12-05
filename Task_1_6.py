# 1. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


from Lesson_6_task_7 import *
from sys import argv


if __name__ == '__main__':
	elements = argv[1:].split('.')
	print(check_date(*(int(element) for element in elements)))
