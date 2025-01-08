"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""


def deposit(balance):
    amount = float(input('Enter the amount to deposit: '))
    balance += amount
    print(f'Account credited with {amount}. Current balance: {balance}')
    return balance


def purchase(balance, history):
    amount = float(input('Enter the purchase amount: '))
    if amount > balance:
        print('Insufficient funds.')
    else:
        item = input('Enter the name of the purchase: ')
        balance -= amount
        history.append((item, amount))
        print(f'Purchase {item} for {
              amount} completed. Current balance: {balance}')
    return balance, history


def purchase_history(history):
    if not history:
        print('Purchase history is empty.')
    else:
        for item, amount in history:
            print(f'{item}: {amount}')
    return


def main():
    balance = 0
    history = []

    while True:
        print('1. Deposit')
        print('2. Purchase')
        print('3. Purchase history')
        print('4. Exit')

        choice = input('Choose an option: ')
        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance, history = purchase(balance, history)
        elif choice == '3':
            purchase_history(history)
        elif choice == '4':
            break
        else:
            print('Invalid option')


if __name__ == "__main__":
    main()
