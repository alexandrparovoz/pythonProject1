if __name__ == '__main__':

# ищем махимальное число в последовательности

    a = int(input())
    maximum = a
    while a != 0:
        if maximum < a:
            maximum = a
        a = int(input())  #  важно переменную поставить в один ряд с ифом
    print(maximum)





