if __name__ == '__main__':

# вещи Василия. Вычислить их общий вес
    vasia = {'books': [700, 5], 'pencil': [50, 7], 'notebooks': [70, 8], 'sweets': [20, 10]}

    weight = 0
    for i in vasia.values():
        weight = weight + (i[0] * i[1])
    print('Общая масса вещей равна -',weight, 'граммов.')
