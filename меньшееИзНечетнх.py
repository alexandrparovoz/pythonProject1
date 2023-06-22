if __name__ == "__main__":

#  вывести наименьшее нечетное
# если его нет, вывести ноль
    a = []
    n = int(input())
    minOdd = []
    for i in range(n):
        a.append(int(input()))
    print(*a)
    for i in range(n):  #  У КИРИЛЛА БЫЛ СПИСОК А И БЕЗ РЕНДЖА И ЭТО ОШИБКА !!!!
        if a[i] % 2 != 0:
            minOdd.append(a[i])
        minOdd.sort()
    if minOdd == []:
        print(0)
    else:
        print(minOdd[0])

