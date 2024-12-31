def matrixDotProduct(a,b):
    c=[[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

print(matrixDotProduct([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]]) )# [[58, 64], [139, 154]