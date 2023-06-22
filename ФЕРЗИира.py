if __name__ == '__main__':

#  узнаем бъет ли кроль короля  на существующих позициях
    n = 6
    x = [2, 4, 2, 4, 1, 6]
    y = [3, 2, 6, 8, 4, 7]
    # n = 8
    # x = []
    # y = []
    # for i in range(n):
    #     x.append(int(input()))
    #     y.append(int(input()))
    # print(x, y)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (abs(x[i] - x[j]) == 1 and abs(y[i] - y[j] == 1) or x[i] == x[j] and abs(y[i] - y[j]) == 1 or abs(x[i] - x[j]) == 1 and y[i] == y[j]):
                count += 1
                break
    if count != 0:
        print("yes")
    else:
        print('No')
