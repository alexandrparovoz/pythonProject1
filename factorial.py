if __name__ == '__main__':

# вывести  результат работы факториала

    fact_num = int(input())
    multi = 1
    for i in range(1, fact_num + 1):
        multi = multi * i
    print(multi)