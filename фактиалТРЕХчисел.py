#  вывести факториал каждого из трех чисел
#  фунция не VOID  т.как имеет в выводе RETURN

def factThree(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    return f

if __name__ == '__main__':

    print(factThree(7))
    print(factThree(8))
    print(factThree(9))