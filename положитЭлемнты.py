if __name__ == '__main__':

    maxElements = int(input('Введите число элементов:'))
    myList = []
    count = 0
    i = 1
    while i <= maxElements:
        myList.append(int(input('Введите элементы :')))
        i += 1
    print(myList)
    for j in myList:
        if j > 0:
            count += 1
    print(count)