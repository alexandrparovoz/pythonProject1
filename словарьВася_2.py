if __name__ == '__main__':

# вещи Василия. Вычислить их наибольшее количество
    vasia = {'books':[700, 5], 'pencil':[50, 7], 'notebooks':[70, 8], 'sweets':[20, 10]}


    max = 0
    for i in vasia.values():
        if i[1] > max:
            max = i[1]
    print('Наибольшее количество вещей равнo ', max, 'штук.')
