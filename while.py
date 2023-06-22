if __name__ == '__main__':

    a = int(input())
    i = 0
    if a % 2 == 0:
        i = a
    else:
        i = a - 1
    while i >= 2:
        print(i)
        i = i - 2