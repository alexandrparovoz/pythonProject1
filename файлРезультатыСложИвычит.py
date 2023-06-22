# пытаюсь проверить результаты вычислений

if __name__ == '__main__':
    list1 = []
    num = 0
    result = ''
    for i in open('test.txt', 'r'):
        list = i.split(' ')
        list1.append(i)
        num = int(list[0])
        for j in range(2, len(list) - 2, 2):
            if list[j - 1] == '-':
                num -= int(list[j])
            if list[j - 1] == '+':
                num += int(list[j])
                if len(num) == 2:
                    if num == int(list1[-2: -1]):
                        result = "True"
                    else:
                        result = 'False'
                else:
                    if num == list1[-1]:
                        result = 'True'
                    else:
                        result = 'False'
        # f = open('output.txt', 'w')
        # f.write(result)
        # f.close()
        print(num)
        print(list1)
        num = 0
