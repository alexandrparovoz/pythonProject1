if __name__ == '__main__':

    # ищем максим расстояние между  максимумами

    pre_num = int(input())
    num = int(input())
    post_num = int(input())

    count = 0
    max_count = 0
    max_num = - 2 ** 31

    if pre_num < num > post_num:
        max_num = num
        count = 1
    else:
        count = 0

    while post_num != 0:
        if not (pre_num < num > post_num):
            count += 1
        if post_num >= num or post_num >= max_num:
            count += 1
        if post_num <= num or post_num <= max_num:
            count += 1
            if max_count < count:
                max_count = count
        else:
            max_num = num
        pre_num = num
        num = post_num
        post_num = int(input())
    print('Расстояние между максиммами равно', max_count - 2)