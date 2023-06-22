#  вывести количество букв и цифр в строке
#  фунция  VOID  т.как имеет в выводе PRINT

def isDigits(a):
    words = 0
    digits = 0
    for i in a:
        if i.isdigit():
            digits += 1
        else:
            words += 1
    print('Digits are ', digits, ', words are ', words)

if __name__ == '__main__':

    a = input()
    isDigits(a)