if __name__ == '__main__':

    pre_num = int(input())
    num = int(input())

    count = 1
    max_count = count

    if pre_num == num:
        count += 1

    while num != 0:
        pre_num = num
        num = int(input())
        if num == pre_num:
            pre_num = num
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1  # не забываем оставлять счетчик на единице, если нет совпадений
    print(max_count)


