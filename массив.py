if __name__ == '__main__':

    n = int(input())
    m = int(input())
    max = n * m
    count = 0
    mass = []
    a = 1
    c = 1
    for i in range(1, max + 1):
        mass.append(i)
        i += 1
        for i in range(1, max + 1):
            c = c + 1
            a = a + c
            print('%4d' % a, end='')
            for j in range(1, max + 1):
                print('%4d' % (a + c), end='')
            print()
