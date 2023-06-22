def older(a):
    old = 0
    name = ''
    for key, item in a.items():
        if item > old:
            old = item
            name = key
    return name



if __name__ == '__main__':

    a = {'ivan': 19, 'alex': 55, 'Eva': 22}
    print(older(a))