def get_neighbors(i, j, matrix):
    neighbors = []
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    for ix, jx in moves:
        newi = i + ix
        newj = j + jx
        if newi >= 0 and newi < len(matrix) and newj >= 0 and newj < len(matrix[0]):
            neighbors.append((newi, newj))

    return neighbors

def find_size(i, j, matrix):
    size = 1
    for newi, newj in get_neighbors(i, j, matrix):
        if matrix[newi][newj] == 1:
            matrix[newi][newj] = -1
            size += find_size(newi, newj, matrix)

    return size

def riverSizes(matrix):
    sizes = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1:
                matrix[i][j] = -1
                sizes.append(find_size(i, j, matrix))

    return sizes

print("Output: " + str(riverSizes([
    [1,0,0,1,0],
    [1,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,1,0]])))
print("Expected: [1, 2, 2, 2, 5]")
