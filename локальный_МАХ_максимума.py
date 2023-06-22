if __name__ == '__main__':

    # ищем МАКСИМАЛЬНЫЙ локальный максимум

    pre_num = int(input())
    num = int(input())
    post_num = int(input())

    local_max = -2 ** 31  #  минимальное значение целого числа в компе , а максимальное значение  2 ** 31
    while post_num != 0:
        if num > post_num and num > pre_num:
            if local_max < num:
                local_max = num
        pre_num = num
        num = post_num
        post_num = int(input())

    print('Локальный максимум равен', local_max)