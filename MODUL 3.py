money_ = 0
buy_dict = {'одежда, руб.': 30000, 'косметика, руб.': 80000,
            'автозапчасти, руб.': 990000}
inverse_buy_dict = {buy_dict[k]: k for k in buy_dict}
my_buy_dict = {}

while True:
    if money_ == 0:
        print('На вашем счёте 0 руб.')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
    choice = input('Выберите пункт меню:')

    if choice == '1':
        while True:
            z = int(input('Введите сумму:'))
            money_ = money_ + z
            print(f'У вас на счете {money_} руб.')
            choice = input('Выберите пункт меню:')
            if money_ == max(buy_dict.values()):
                print((buy_dict))
            break

    if choice == '2':
        while True:
            sum_buy = int(input('Введите сумму покупки:'))
            if money_ < sum_buy:
                print('у Вас недостаточно средств')
                choice = input('Выберите пункт меню:')
            if money_ >= sum_buy:
                key = inverse_buy_dict.get(sum_buy)
                money_ = money_ - sum_buy
                my_buy_dict[sum_buy] = key
                print(f'мои покупки {my_buy_dict}')
                print(f'У вас на счете {money_} руб.')
                choice = input('Выберите пункт меню:')
            break

    if choice == '3':
        while True:
            print(f'мои покупки {my_buy_dict}')
            break

    if choice == '4':
        break
