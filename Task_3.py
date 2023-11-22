# 3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один
# допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

MAX_WEIGHT = 15
items = {'tent': 5, 'water': 3, 'food': 2, 'clothes': 3, 'first aid kit': 1, 'flashlight': 2, 'sleeping bag': 3, 'dishes': 2}
possible_items = []
for item, weight in items.items():
        if weight <= MAX_WEIGHT:
            possible_items.append(item)
            MAX_WEIGHT -= weight

print(possible_items)