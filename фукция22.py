
#  если есть скобки то это функция
#  функцию пишем на уровне  if

def factorial(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    print(f)


if __name__ == '__main__':
    a = add(1, 2)
    print (a)