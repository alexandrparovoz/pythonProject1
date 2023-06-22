#  вывести самое длинное слово в строке
#  фунция не VOID  т.как имеет в выводе RETURN

def bigWord(a):
    a = a.split(' ')
    length = 0
    maxWord = ''
    for i in range(len(a)):
        if len(a[i]) > length:
            length = len(a[i])
            maxWord = a[i]
    return maxWord

if __name__ == '__main__':

    a = input()
    print('Самое длинное слово это -', bigWord(a))

