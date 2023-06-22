#  решаем, является строка ПОЛИНДРОМОМ или нет


def palindrom(a):
    b = a[:: -1]
    if a == b:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    a = input()
    string = palindrom(a) # передаем переменной  sting  выводы функции palindrom()
    print(string)

