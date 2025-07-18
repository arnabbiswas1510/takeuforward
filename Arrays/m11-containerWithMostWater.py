def maxArea(arr):
    i,j=0,len(arr)-1
    maxArea=0
    while i < j:
        maxArea = max(maxArea, min(arr[i],arr[j])*(j-i))
        if arr[i] < arr[j]: #I got the comparison operator wrong the first time
            i+=1
        else:
            j-=1
    return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))