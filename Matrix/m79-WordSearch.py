"""
Uses backtracking
"""
def searchNext(matrix, word, rows, cols, i, j, idx):
    found = False
    if idx == len(word):
        return True
    if i < 0 or j < 0 or i >= rows or j >= cols or matrix[i][j] != word[idx] or matrix[i][j]=="X" :
        return False
    c=matrix[i][j]
    matrix[i][j]="X" #Do this instead of adding i,j to a set and incur extra storage
    #We dont need any if condition before each of these recursive calls since in line 5 we are checking if the adjacent
    # cell is already visited
    found |= searchNext(matrix, word, rows, cols, i, j + 1, idx + 1)  #right
    found |= searchNext(matrix, word, rows, cols, i + 1, j, idx + 1) #down
    found |= searchNext(matrix, word, rows, cols, i - 1, j, idx + 1) #Up
    found |= searchNext(matrix, word, rows, cols, i, j - 1, idx + 1) #Left
    matrix[i][j]=c
    return found

def exists(matrix, word):
    rows=len(matrix)
    cols=len(matrix[1])
    idx=0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == word[idx]:
                if searchNext(matrix, word, rows, cols, i, j, idx):
                    return True
    return False

print(exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))