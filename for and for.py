if __name__ == '__main__':

    a = int(input())
    b = int(input())

    if a % 2 != 0:
        a = a + 1
    for i in range(a, b, 2):
        print(i)