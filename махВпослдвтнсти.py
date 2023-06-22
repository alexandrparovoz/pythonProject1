if __name__ == '__main__':
#  найти максимум в последовательности


    a = int(input())
    i = 0
    maxim = a
    while a != 0:
        if maxim < a:
            maxim = a
        a = int(input())
    print(maxim)