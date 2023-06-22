if __name__ == '__main__':
# узнаем точно ли заданное число явл степенью двойки
    a = int(input())
    y = 1
    i = 2
    while i < a:
        y = y + 1
        i = 2 ** y
    if i == a:
        print('yes')
    else:
        print('No')
