#  вывести факториал каждого из трех чисел
#  функция  VOID  т.как имеет в выводе print

def factThree(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    print(f)

if __name__ == '__main__':

    a = int(input())
    b = int(input())
    c = int(input())

    factThree(a)
    factThree(b)
    factThree(c)