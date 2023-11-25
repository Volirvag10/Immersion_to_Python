# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно
# сохраняйте все операции поступления и снятия средств в список.

def deposit(balance, amount):
    # Пополнение счета
    if amount % 50 != 0:
        print("Сумма пополнения должна быть кратной 50 у.е.")
        return balance  # Если сумма не кратна 50, возврат без изменения баланса
    balance += amount
    print(f"Вы пополнили счет на {amount} у.е.")
    return balance


def withdraw(balance, amount):
    # Снятие средств
    if amount % 50 != 0:
        print("Сумма снятия должна быть кратной 50 у.е.")
        return balance  # Если сумма не кратна 50, возврат без изменения баланса
    if amount > balance:
        print("Недостаточно средств на счете.")
        return balance  # Если недостаточно средств, возврат без изменения баланса

    wealth_tax = 0.10  # Налог на богатство 10%
    if balance > 5000000:
        amount_with_tax = amount + (amount * wealth_tax)
        if amount_with_tax < 30:
            amount_with_tax = 30
        elif amount_with_tax > 600:
            amount_with_tax = 600
    else:
        amount_with_tax = amount
    balance -= amount_with_tax
    print(f"Вы сняли {amount_with_tax} у.е.")
    return balance


def apply_interest(balance, transactions):
    # Начисление процентов
    if transactions % 3 == 0:
        interest = 0.03 * balance
        balance += interest
        print(f"Начислены проценты: {interest} у.е.")
    return balance


def check_balance(balance):
    # Проверка баланса
    print(f"Ваш баланс: {balance} у.е.")


def atm_menu():
    balance = 0
    transactions = 0
    while True:
        print("\nМеню банкомата:")
        print("1. Пополнить счет")
        print("2. Снять средства")
        print("3. Выйти")
        choice = input("Выберите действие (1/2/3): ")
        if choice == '1':
            amount = int(input("Введите сумму для пополнения: "))
            balance = deposit(balance, amount)
            check_balance(balance)
            transactions += 1
            balance = apply_interest(balance, transactions)
        elif choice == '2':
            amount = int(input("Введите сумму для снятия: "))
            balance = withdraw(balance, amount)
            check_balance(balance)
            transactions += 1
            balance = apply_interest(balance, transactions)
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


atm_menu()
