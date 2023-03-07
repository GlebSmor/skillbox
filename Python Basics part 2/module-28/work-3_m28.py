class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f'День: {self.day}   Месяц: {self.month}   Год: {self.year}'

    @classmethod
    def is_date_valid(cls, date: str):
        try:
            day, month, year = date.split('-', maxsplit=2)

            day, month, year = int(day), int(month), int(year)
            month_31 = [1, 3, 5, 7, 8, 10, 12]
            month_30 = [4, 6, 9, 11]

            if month in month_31 and 1 <= day <= 31 and year > 0:
                return True

            elif month in month_30 and 1 <= day <= 30 and year > 0:
                return True

            elif month == 2 and 1 <= day <= 28 and year > 0:
                # с високосными годами не стал заморачиваться =)
                return True

            else:
                return False
        except ValueError:
            print('Введена некорректная дата введите в формате dd-mm-yyyy')

    @classmethod
    def from_string(cls, date: str):
        try:
            day, month, year = date.split('-', maxsplit=2)
            date_obj = cls(int(day), int(month), int(year))
            return date_obj
        except ValueError:
            print('Введена некорректная дата введите в формате dd-mm-yyyy')


date_ex = Date.from_string('10-12-2077')
print(date_ex)
print(Date.is_date_valid('28-2-2077'))
print(Date.is_date_valid('40-12-2077'))