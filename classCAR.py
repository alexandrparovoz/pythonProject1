#  работа с экземплярами и классами

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
# позже добавляем аргумент по умолчанию
        self.odometerReading = 0

    def discriptiveName(self):
#  возвращает аккуратно сформатированное описание авто
        longName = f'{self.year} {self.make} {self.model}'
        return longName.title()

# позже добавляем метод readingOdometer
    def readingOdometer(self):
        print(f'This car has {self.odometerReading} miles on it.')

if __name__ == '__main__':

    myNewCar = Car('audi', 'a4', 2019)
    print(myNewCar.discriptiveName())
    myNewCar.readingOdometer()