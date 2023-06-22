if __name__ == '__main__':

# вещи Василия. Вычислить самую тяжелую вещь

    vasia = {'books':[700, 5], 'pencil':[50, 7], 'notebooks':[70, 8], 'sweets':[20, 10]}

    weight = 0
    max = 0
    keys = vasia.keys()
    keys = list(keys)
    c = 0
    key = [c]
    keyMax = ''
    for i in vasia.values():
        for j in i:
            if j == i[0]:  #  почему то не могу применить j[0]  или j[1]
                weight = i[0]
                key = keys[c]
                c += 1
                if weight > max:
                    max = weight
                    keyMax = key
                weight = 0
    print('Самая тяжелая', keyMax,'равна', max, 'граммов.')
