if __name__ == '__main__':

# возведение в степень без методов
# без ELIF у меня никак не получалось вывести только один принт

    a = int(input())
    b = int(input())
    if a == 0 and b != 0:
        print('False')
    elif a != 0 and b == 0:
        print(1)
    else:
        count = a
        for i in range(1, b):
            count = count * a
        if count < 0:
            count = count * (-1)
        print(count)