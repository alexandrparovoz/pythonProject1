#  сначала находим факториал числа
#  следующая функция принимает результат факториала и решает
#  ЧЕТНОЕ или НЕЧЕТНОЕ число

def factorial(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    ifOdd(f)

def ifOdd(f):
    if f % 2 != 0:
        print('Odd')
    else:
        print('Even')

if __name__ == '__main__':

    a = int(input())
    factorial(a)  # если убрать инпут, то сразу в переменную а вводим нужное число