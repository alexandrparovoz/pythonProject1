#  функция поиска неповторяющихся цифр в массиве
#  с применением VOUD
#  с RETURN выводит только первую (одну) цифру

def unicDigits(a):
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == a[j]:  # если позиции не равны. а числа равные. то BREAK
                break
        else:
            print(a[i], end=' ')   # почему нe могу сделать с помощью RETURN

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))   # как все это запихнуть в функцию
    unicDigits(a)