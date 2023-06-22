if __name__ == '__main__':

# находим ЗАГЛАВНЫЕ БУКВЫ и считаем их оличество через Unicode
    a = input()
    b = len(a)
    count = 0
    for i in range(b):
        if 64 < ord(a[i]) < 91: # заглавные латинские в юникоде от 65 до 90
            count += 1
    print(count)




