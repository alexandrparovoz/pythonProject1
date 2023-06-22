if __name__ == "__main__":

# посчитать пары элементов (их количество)

    a = []
    n = int(input())
    for i in range(n):
        a.append(int(input()))
    print(*a)
    count = 0
    i = 1
    for i in range(n):
        c = 0
        preNum = a[c]
        if a[i] == preNum:
            count += 1
        c += 1
    print(count)