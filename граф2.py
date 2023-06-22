# вторая версия графа

def minWay(a, b):
    wayAB = 0
    way = 2 ** 31
    smallWay = 0
    if graph[a][b] != -1:
        wayAB = graph[a][b]
    row = a
    nextRow = a
    count = 0
    visited = []
    while count < len(graph):
        for i in range(len(graph[row])):
            if graph[row][i] == -1 or [row, i] in visited:
                continue
            if graph[row][i] < way:
                way = graph[row][i]
                nextRow = i
        count += 1
        visited.extend([[row, nextRow]])
        visited.extend([[nextRow, row]])
        smallWay += way
        way = 2 ** 31
        row = nextRow
    return smallWay




if __name__ == '__main__':
    graph = [[-1, 2, 1, 2, -1],
             [2, -1, 4, 0, 3],
             [1, 4, -1, 2, -1],
             [2, 0, 2, -1, 3],
             [-1, 3, -1, 3, -1]]

    print(minWay(0, 2))