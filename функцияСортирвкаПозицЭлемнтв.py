#  сортировка позиционных элементов
#

def sortElem(*args):
    a = []
    for elem in args:
        a.append(elem)
        a.sort()

    print(*a)


if __name__ == '__main__':
    sortElem('were', 'more', 'out', 'must','without' )

