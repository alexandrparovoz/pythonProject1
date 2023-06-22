if __name__ == '__main__':

    a = [1, 2, 4, 6, 4, 22, 8, 5, 4]
    max = 0

    for i in range(1, len(a) - 1):
        if a[i] > a[i - 1] and a [i] > a[i + 1]: # ищем елемент по индексу
            max = a[i]
    print(max)


