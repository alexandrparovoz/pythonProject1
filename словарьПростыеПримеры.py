if __name__ == '__main__':

    a = {'egor': 12, 'vasia': 32, 'sergey': 40}
    #  находим сумму значений (одиночных)
    sum = 0
    for i in a.values():
        sum = sum + i
    print(sum)

    #  находим сумму Unicode  по значению
    sum2 = 0
    for i in a:
        for j in i:
            sum2 = sum2 + ord(j)
    print('сумма',sum2)

    # находим сумму Unicode  по  ключам
    sum2 = 0
    for i in a:  # делаем перебор ключей в словаре А
        for j in i:  # делаем перебор в символах самого ключа
            sum2 = sum2 + ord(j)
    print('сумма',sum2)

    c = {'egor':[23, 2, 12] , 'vasia': [32, 92, 3] ,'sergey': [40, 21, 3]}
    sum3 = 0
    for i in c:
        for d in c.values():
            sum3 = sum3 + d
        print('сумма листов', sum3)



