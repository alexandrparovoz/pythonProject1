if __name__ == '__main__':

    a = int(input())
    pow_a = int(input()) # надо еще узнать как кое число большее

    temp = a

    for i in range(pow_a - 1):
        a = a * temp
        print(a)
    print('Конечное число:', a)
