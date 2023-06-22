# еще одна попытка написать маршрут графа
if __name__ == '__main__':
    graph = [[-1, 2, 1, 2, -1],
             [2, -1, 4, 0, 3],
             [1, 4, -1, 2, -1],
             [2, 0, 2, -1, 3],
             [-1, 3, -1, 3, -1]]
    way = 2 ** 31
    smallWay = 0
    row = 0
    newrow = 0
    visited =[]
    i = 0
    while i < len(g):
        for i in graph[row]:
            visited.append(newrow)
        for j in range(len(graph)):
            if graph[i][j] == -1:
                continue
            if graph[i][j] < way:
                way = graph[i][j]
                newrow = j
        smallWay += way
        row = newrow
        way = 0

    print(smallWay)


