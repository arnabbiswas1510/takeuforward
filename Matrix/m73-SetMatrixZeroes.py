def markRow(i, matrix):
    for c in range(len(matrix[0])):
        if matrix[i][c]!= 0:
            matrix[i][c]= "X"
"""
Had some trouble with markRow and markCol and needed some debugging to get the indexes right
"""
def markCol(j, matrix):
    for r in range(len(matrix)):
        if matrix[r][j]!= 0: #Forgot to include this line initially in bot methods and needed to debug
            matrix[r][j]= "X"
"""
Brute force - In first traversal mark all rows and columns as X (assuming that is not taken). Except for cells that are 0
Second traversal mark all Xs to 0. n^3 time
"""
def setZeroes1(matrix):#Brute n^3
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                markRow(i, matrix)
                markCol(j, matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "X":
                matrix[i][j] = 0
    return matrix
"""
Here you mark the rows and columns in 2 separate arrays and in next traversal set the 0s
n^2 time but n^2 space
"""
def setZeroes2(matrix):#Better
    row = [-1]*len(matrix)
    col = [-1]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i]=0
                col[j]=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i] == 0 or col[j] == 0: #Note this is OR and not AND
                matrix[i][j] = 0
    return matrix

def setZeroes3(matrix):#Optimal
    col0=1 #U need this because you want to distinguish the mat[0,0] cell which will be used by both col0 and row0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0]=0
                if j==0:
                    col0=0
                else:
                    matrix[0][j] = 0
    for i in range(1,len(matrix)): #Make sure you start from 2nd col here and below
        for j in range(1,len(matrix[0])):
            if matrix[i][0] == 0 or matrix[0][j] == 0: #Note this is OR and not AND
                matrix[i][j] = 0
    #Finally you address the 0th row and column. But u need to fix row0 before col0. Why?
    #Because if col0==0 then you will set matrix[0,0]=0 and then below if condition will get compromised
    if matrix[0][0] == 0:
        for j in range(len(matrix[0])):
            matrix[0][j]=0
    if col0 == 0:
        for i in range(len(matrix)):
            matrix[i][0]=0
    return matrix

print(setZeroes2([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(setZeroes3([[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]))