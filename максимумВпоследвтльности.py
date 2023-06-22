if __name__ == '__main__':
# выводим максимум в последовательности
    a = []
    n = int(input())
    minOdd = []
    for i in range(n):
        a.append(int(input()))
    print(*a)
    max = a[0]
    for i in range(n):
        if a[i] > max:
            max = a[i]
    print(max)

