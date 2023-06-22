def vowels(a):

    w = ['a', 'e', 'y', 'u', 'i', 'o', ]
    count = 0
    for i in a:
        for j in w:
            if i == j:
                count += 1
                break  # можно ставитьь брей чтобы дальше не искал
    return count



if __name__ == '__main__':

    a = input()
    print(vowels(a))