if __name__ == '__main__':

# итерирование двухмерного массива

    n = int(input())
    m = int(input())
    mass = []
    x = 1
    for i in range(n):
        small_mass = []
        for j in range(m):
            small_mass.append(j + x)
            x += 1
        mass.append(small_mass)  
    print(mass)
# вывод двхмерного массива

    for i in mass:
        for el in i:
            print(el, end='\t')
        print()
