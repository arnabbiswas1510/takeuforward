import sys

def searchMin(arr):
    start, end = 0, len(arr)-1
    minimum = sys.maxsize
    while start <= end: #Why = ?
        mid = start + (end-start)//2
        if arr[mid] < arr[end]: #The latter half is the sorted half eg [4,5,1,2,3]
            minimum=min(minimum, arr[mid])
            start=mid+1
        else: #First half is sorted eg [2,3,4,5,1]
            minimum=min(minimum, arr[start])
            end=mid-1
    return minimum

print(searchMin([5,6,7,3,4]))
print(searchMin([7,3,4,5,6]))
