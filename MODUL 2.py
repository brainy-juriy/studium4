
def year_born():
    _year_ = input('Введите год рождения А.С.Пушкина:')
    while _year_ != '1799':
        print("Не верно")
        _year_ = input('Введите год рождения А.С.Пушкина:')
    print('Верно')

year_born()


def day_born():
    _day_ = input('Введите день рождения Пушкин?')
    while _day_ != '6':
        print("Не верно")
        _day_ = input('В какой день июня родился Пушкин?')
    print('Верно')

day_born()


