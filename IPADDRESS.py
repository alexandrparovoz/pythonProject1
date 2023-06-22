if __name__ == '__main__':
#  что то не работает
# что то не то с отступами (повторяются принты)

    a = input()

    b = a.split('.')
    if len(b) == 4:
        for i in b:
            if int(i) > 255 or int(i) < 0:
                print('no')
                break
        print('yes')
    else:
        print('no')