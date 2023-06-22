if __name__ == '__main__':

# нaходим четные  индексы в списке

    maxElements = int(input('Введите число элементов:'))
    myList = []
    newList = []
    i = 1
    j = 0
    while i <= maxElements:
        myList.append(int(input('Введите элементы :')))
        i += 1
    print(myList)
    while j <= len(myList):
        newList.append(myList[j])
        j = j + 2
    print(newList)

    # while count <= maxElements:
    #     for i in myList:
    #         print(myList[i])int(input('Введите элементы через пробл:'
    #         i = i + 2
    #     count += 1
