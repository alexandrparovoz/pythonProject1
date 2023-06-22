#  вывести элемент  с  самым  длинным  ключом
#

def longestKey(**kwargs):
    longer = 0
    longerKeyItem = ''
    for keys, items in kwargs.items():
        if len(keys) > longer:
            longer = len(keys)
            longerKeyItem = items
    print('Самый длинный ключ - зто ', longer)
    print('Его  значение - это ', longerKeyItem)

if __name__ == '__main__':
    longestKey(speedyRiver='yangtze', longestRiver='amazon', wideRiver='laPlata', dirtyRiver='citarum',
               shortRiver='reprua', clearRiver='versasca')

