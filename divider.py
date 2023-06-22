if __name__ == '__main__':
#  есть период от M до N. Найти делители (без остатка)
# за исключением единицы и самого числа

    m = int(input())
    n = int(input())
    num = 0
    divider = 0
    num2 = 2
    for i in range(m, n + 1):
        num = i
        for num2 in range(2, num):
            if num % num2 == 0:
                divider = num2
                print(num,' - ', divider)

