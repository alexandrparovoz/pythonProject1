if __name__ == '__main__':

    maxElements = int(input('Введите число элементов:'))
    myList = []
    newList = []
    i = 1
    while i <= maxElements:
        myList.append(int(input('Введите элементы :')))
        i += 1
    print(myList)
    preNum = myList[0]
    for j in myList:
        if j > preNum:
            newList.append(j)
            preNum = j
    print(newList)