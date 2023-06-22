if __name__ == '__main__':

# вещи Василия. Вычислить вещь, все экземпляры которой весят меньше всех

    vasia = {'books':[700, 5], 'pencil':[50, 7], 'notebooks':[70, 8], 'sweets':[20, 10]}

    keys = vasia.keys()
    keys = list(keys)
    # следующие три строки были посвящены тому,
    # чтобы взять за минимум произвдение в эначении первого ключа
    firstkey = keys[0]
    firstValue = vasia[firstkey]
    min = firstValue[0] * firstValue[1]
    weight = 0
    c = 0
    key = [c]
    keyMin = ''
    for i in vasia.values():
        for j in i:
            if j == i[0]:
                weight = i[0] * i[1]
                key = keys[c]
                c += 1
                if weight < min:
                    min = weight
                    keyMin = key
                weight = 0
    print('Все экземпляры', keyMin, 'весят всего', min)