# впервые создаем класс это ласс собак

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
#  tеперь соэдаем функцию для команды СИДЕТЬ
    def sit(self):
        print(self.name.title(), ', sitting!')

#  tеперь соэдаем функцию для команды КРУТИТЬСЯ
    def rollOver(self):
        print(self.name.title(), ', rolling over!')

#  создаем экземпляр класса

myDog = Dog('villie', 5)
print('My dog name is', myDog.name.title())
print('My dog is', str(myDog.age), 'years old.\n')

# вызываем методы класса СОБАКА

myDog.sit()
myDog.rollOver()