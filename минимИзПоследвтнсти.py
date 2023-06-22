if __name__ == "__main__":

# находим наименьшее из положительных

    a = []
    n = int(input())
    posNumber = []
    for i in range(n):
        a.append(int(input()))
    print(a)
    for i in range(n):
        if a[i] > 0:
            posNumber.append(a[i])
            posNumber.sort()
    print(posNumber[0])

