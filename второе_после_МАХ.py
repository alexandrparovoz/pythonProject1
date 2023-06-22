if __name__ == '__main__':

    a = int(input())
    b = int(input())

    max = 0
    pre_max = 0
    if a > b:               # выясняем. какая переменная из двух максимальна
        max = a
        pre_max = b
    else:
        max = b
        pre_max = a

    while a != 0:
        if a > max:
            pre_max = max   # обязательно сначала меняем старое на новое значения в pre_max
            max = a         #  и только потом в переменной max
        if a < max and a > pre_max:
            pre_max = a
        a = int(input())
    print(pre_max)