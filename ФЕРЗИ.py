if __name__ == '__main__':

#  бъют ли короли друг друга
#  не работает почему то


    n = 4
    a = [[2, 3], [4, 5], [6, 8], [7, 7]]
    # for i in range(n):
    #     b = []
    #     for j in range(2):
    #         b.append(int(input()))
    #     a.extend([b])
    # print(a)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][0] == a[j][0] and ((a[i][1] + 1) == a[j][1] or (a[i][1] - 1) == a[j][1]):
                count += 1
                break
            if (a[i][0] + 1) == a[j][0] and ((a[i][1] + 1) == a[j][1] or ([i][1] - 1) == a[j][1] or a[i][1] == a[j][1]):
                count += 1
                break
            if (a[i][0] - 1) == a[j][0] and ((a[i][1] + 1) == a[j][1] or ([i][1] - 1) == a[j][1] or a[i][1] == a[j][1]):
                count += 1
                break
    if count != 0:
        print('Yes')
    else:
        print('No')