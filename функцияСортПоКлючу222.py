#  сортировка непозиционных элементов по ключу  через  sorted
#  как то даже очень просто

def sortKey(**kwargs):
    for key in sorted(kwargs.keys()):
        print(key, kwargs[key])


if __name__ == '__main__':
    sortKey(speedyRiver='yangtze', longestRiver='amazon', wideRiver='laPlata', dirtyRiver='citarum',
               shortRiver='reprua', clearRiver='versasca')
