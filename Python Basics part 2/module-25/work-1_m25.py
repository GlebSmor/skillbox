class Property:

    def __init__(self, worth):
        self.worth = self.set_worth(worth)

    def set_worth(self, worth):
        if worth > 0:
            return worth
        else:
            raise ValueError('Значение должно быть больше 0')

    def get_worth(self):
        return self.worth

    def tax(self):
        return self.worth


class Apartment(Property):
    name = 'Квартиру'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    name = 'Машину'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    name = 'Дачу'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


print('*** Расчет ваших налогов ***\n')

car = float(input('Введите цену машины: '))
apartment = float(input('Введите цену квартиры: '))
house = float(input('Введите цену дачи: '))

money = float(input('Введите кол-во ваших денег: '))

tax_list = [Car(car), Apartment(apartment), CountryHouse(house)]
summa = 0
print()
for elem in tax_list:
    print(f'Налог на "{elem.name}" == {elem.tax()}')
    summa += elem.tax()

print('\nОбщая сумма налогов ==', summa)

if money < summa:
    print('Вам не хватает: ', summa - money)
else:
    print('После уплаты налогов останется: ', money - summa)


