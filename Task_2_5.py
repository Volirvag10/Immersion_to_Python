# 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.

import decimal


def list_of_bonuses(names: list[str], bets: list[int], rewards: list[str]) -> dict[str, decimal.Decimal]:
    gen_dict = {names: (bets * decimal.Decimal(rewards[:-1]) / 100) for names, bets, rewards in
                zip(names, bets, rewards)}
    return gen_dict


a = ['Ivan', 'Boris', 'Sasha']
b = [100000, 75000, 65000]
c = ['10%', '15%', '20%']
print(list_of_bonuses(a, b, c))