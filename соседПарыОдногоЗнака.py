if __name__ == '__main__':

#  вывести два соседних элемента если они одного знака

    maxElements = int(input('Введите число элементов:'))
    myList = []
    newList = []
    i = 1
    while i <= maxElements:
        myList.append(int(input('Введите элементы :')))
        i += 1
    print(myList)
    preNum = myList[0]
    for j in myList[1:]:
        if j * preNum > 0:  # через умножение мы понимаем, оба числа положтльны или отрицательны
            newList.extend([preNum, j])
            break
        preNum = j
    print(*newList)  #  спомощью звездочки убираем квадр скобки