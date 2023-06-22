if __name__ == '__main__':
# найти локальный максимум в последвтлнсти
# было трудно, одним глазом подсмотрел


    num1 = int(input())  # задаем отдельно первое и второе число
    num2 = int(input())
    count = 0
    while num1 != 0 and num2 != 0:
        a = int(input())
        if num1 < num2 and a < num2 and a != 0:  # не включаем крайний ноль
            num1 = num2  # передвигаем переменные на одно число вправо
            num2 = a
            count += 1
        else:
            num1 = num2
            num2 = a
    print('Число максимумов равно',count,'.')


