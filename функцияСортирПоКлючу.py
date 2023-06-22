#  сортировка непозиционных элементов по ключу
#

def sortKey(**kwargs):
    a = []
    for key in kwargs.keys():
        a.append(key)
        a.sort()
    for item in a:
        if item in kwargs:
            print(item, kwargs[item])


if __name__ == '__main__':
    sortKey(speedyRiver='yangtze', longestRiver='amazon', wideRiver='laPlata', dirtyRiver='citarum',
               shortRiver='reprua', clearRiver='versasca')
