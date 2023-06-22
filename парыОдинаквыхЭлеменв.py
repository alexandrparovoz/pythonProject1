if __name__ == "__main__":

# посчитать пары элементов (их количество)

    a = []
    n = int(input())
    for i in range(n):
        a.append(int(input()))
    print(*a)
    count = 0
    c = 0
    preNum = a[c]
    i = 1
    while i < n:
        if a[i] == preNum:
            count += 1
        # if a[j] == a[j + 1]:
        #     continue
        # preNum = a[item]
        # item += 1
        c += 1
    print(count)