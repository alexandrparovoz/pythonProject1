if __name__ == '__main__':

    a = {'shdhd': 'dd', 'key1':'necne', '322a': 'student'}
    for i in a:  #  выводим ключи
        print(i)
    for i in a.values():  #  выводим значения
        print(i)
    for i in a.keys():  # снова  выводим ключи
        print(i)

    b = {'egor': 123, 'oleg':'2322', 'genf': '999'},
    max = ' '
    for i in b:   #  поиск самого большого ключа
        if len(i) > len(max):
            max = i
    print('This is',max)