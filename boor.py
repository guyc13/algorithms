def buildmat():
    matrix = [[0 for x in range(4)] for y in range(4)]
    n = 4
    for b in range(4):
        for t in range(4):
            if (b == 1 and (t == 0 or t == 3)) or (b == 2 and (t == 0 or t == 3)) or (b == 0 and t == 3):
                matrix[b][t] = 1;
            else:
                matrix[b][t] = 0;

    for c in range(4):
        print matrix[c]
    print "_" * 100
    return matrix


matrix1 = [[0, 0, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
matrix2 = [[0, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 0], [1, 1, 1, 1]]
matrix3 = [[0, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 0], [1, 1, 1, 1]]
matrix4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matrix5 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

def findpit(mat, n, i=0, j=1):
    while i <= n - 1 and j <= n - 1:  # prevant array out of range
        while True:                   # start runnin until the first pattern of asimetric
            if j > n - 1:
                print "no pit"
                return False

            if mat[i][j] != mat[j][i]:  # looking for [0][1] or [1][0]
                break
            i = max(i, j)
            j = i + 1

        # if j == 1:
        if checkpit(mat, i, n - 1):
                return i
        elif checkpit(mat, j, n - 1):
                return j
        # elif checkpit(mat, j, n - 1):
        #     return j
        i = max(i, j)
    print "no pit"


def checkpit(mat, node, n):
    # check line
    t = 0
    isboor = True
    while t <= n:
        if mat[node][t] == 1:
            isboor = False
        t += 1
    # check coloumn
    t = 0
    while t <= n:
        if mat[t][node] == 0:
            if node != t:
                isboor = False
        t += 1
    return isboor


if __name__ == '__main__':

    #mat = buildmat()
    print "matrix1:"
    for line in range(4):
        print  matrix2[line]
    pit = findpit(matrix1, 4)
    print "-----------\n"
    print pit
