if __name__ == '__main__':

    #  вывод суммы элементов значений  по индексу

    c = {'egor': [23, 2, 12], 'vasia': [32, 92, 3], 'sergey': [40, 21, 3]}
    sum3 = 0
    for i in c:
        for j in c.values():
            sum3 = sum3 + j[2]
    print('сумма листов', sum3)