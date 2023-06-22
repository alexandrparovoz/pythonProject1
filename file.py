if __name__ == '__main__':

    f = open('test.txt', 'w+')
    f.write('28482442\n98765\n2366')
    f.close()
    count = 0
    for i in open('test.txt', 'r'):
        count += 1
    print(count)
