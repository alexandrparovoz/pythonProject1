# создаем граф из пяти вершин и ищем короткий(менее затратный путь)



# создаем функцию для поиска кратчайшего пути между вершинами а и b
def shortWay(a, b):
    way = 2 ** 31
    # wayAB = 0
    # visited = []
    # if graph[a][b] != -1:
    #     wayAB = graph[a][b]
    # if graph[a][b] == -1:
    for i in range(len(graph[a])):
        if graph[a][i] == -1:
            continue
        if graph[a][i] < way:
            way = graph[a][i]
    return way

def generator(a, graph):
    for i, value in enumerate(graph[a]):
        if i > 0:
            yield i







if __name__ == '__main__':
    graph = [[-1, 2, 1, 2, -1],
             [2, -1, 4, 0, 3],
             [1, 4, -1, 2, -1],
             [2, 0, 2, -1, 3],
             [-1, 3, -1, 3, -1]]
    print(shortWay(2,4))