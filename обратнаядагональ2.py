n = int(input())
matrix = []
a = 1
for i in range(n):
    subMatrix = []
    for j in range(n):
        subMatrix.append(a)
        a += 1
    matrix.append(subMatrix)
print(matrix)
b = 0
c = n - 1

for i in range(n - 1):
    b += 1
    c -= 1
    print(matrix[b][c])


