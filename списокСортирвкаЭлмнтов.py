if __name__ == '__main__':

# сортируем  список лексически

    a = [ 'whwh', 'rr', 'etgryu', 'wwwwwwwww']

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:  #  если надо по длине строки то добавим  len
                a[i], a[j] = a[j], a[i]
    print(a)
