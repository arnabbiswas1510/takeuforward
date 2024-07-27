"""
Brute force - Requires n^2 storage since you will be overwriting the cells

Looks like the matrix can only be a SQUARE matrix else you would have to factor in the rotated shape and the algo
below becomes more involved

Follow up question - how to rotate matrix Anti clockwise? Below code is to rotate clockwise
"""

def rotate1(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    ans=[[-1 for i in range(rows)] for j in range(cols)] #Remember this shortcut to init a matrix
    #Simple multiplication like [[-1]*rows]*cols doesnt work in the above
    for i in range(rows):
        for j in range(cols):
            ans[j][cols-1-i] = matrix[i][j] #Write this out to get this
    return ans

def rotate2(matrix): #Optimized with no extra storage
    #Transpose (diagonally swapped and hence no extra space) and reverse
    rows=len(matrix)
    cols=len(matrix[0])
    #Remember the 2 changes below to traverse matrix diagonally
    for i in range(rows-1):#1
        for j in range(i,cols):#2
            matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j] #Write this out to get this
    for i in range(rows):
        matrix[i].reverse() #Inbuilt reverse method which modifies Array in place (like sort)
    return matrix
print(rotate2([[1,2,3],[4,5,6],[7,8,9]]))