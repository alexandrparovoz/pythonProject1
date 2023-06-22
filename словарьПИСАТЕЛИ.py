if __name__ == '__main__':
#  найти самого пишущего писателя(больше всего книг)

    libriary = ({'Bloody moon': 'M.Stivenson', 'Python programming': 'M. Dauson',
                 'The Python Workbook': 'B. Stepherson', 'Capains dother': 'A. Pyshkhin',
                 'Learn Python': 'E. Matith', 'E. Onegin': 'A. Pyshkhin'})
    values = list(libriary.values())
    values.sort()
    count = 1
    maxCount = 0
    maxAuthor = ''
    for i in values:
        author = i
        for j in range(1, len(values)):  # единицу в ренже надо бы увеличивать но, т.к. список
            if author == values[j]:  # отсортирован, я посчитал это лишним
                count += 1
                if count > maxCount:
                    maxCount = count
                    maxAuthor = author
        count = 0  # обнуляем счетчик во время изменения значения  (автора)
    print(maxCount)
    print(maxAuthor)