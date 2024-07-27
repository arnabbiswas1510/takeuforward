def spiralOrder(matrix):
    top=0
    down=len(matrix)-1 #Include the exact boundary of array here and hence -1
    left=0
    right=len(matrix[1])-1
    while True:
        if top > down or left > right:
            break
        for i in range(left, right+1): #For every loop, go from left to right inclusive
            print(matrix[top][i], end=",")
        top+=1
        if top > down or left > right:
            break
        for i in range(top, down+1):
            print(matrix[i][right], end=",")
        right-=1
        if top > down or left > right:
            break
        for i in range(right, left-1, -1): #For every loop, go from left to right inclusive
            print(matrix[down][i], end=",")
        down-=1
        if top > down or left > right:
            break
        for i in range(down,top-1,-1):
            print(matrix[i][left], end=",")
        left+=1

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
