#  вывести факториал каждого из трех чисел
#  фунция не VOID  т.как имеет в выводе RETURN

def factThree(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    return f

if __name__ == '__main__':

    a = int(input())
    b = int(input())
    c = int(input())
# в переменной сохраняю сумму выводов трех функций
    f = factThree(a) + factThree(b) + factThree(c)
    print(f)

