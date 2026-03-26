def search(arr, target):
    start, end = 0, len(arr)-1
    while start <= end: #Why = ?
        mid = start + (end-start)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < arr[end]: #The latter half is the sorted half eg [4,5,1,2,3]
            if arr[mid] <= target <= arr[end]: #Check if target falls in this half
                start=mid+1 #Move to latter half
            else:
                end=mid-1 #Move to first half
        else: #First half is sorted eg [2,3,4,5,1]
            if arr[start] <= target <= arr[mid]: #Follow same logic as above
                end=mid-1
            else:
                start=mid+1
    return -1

print(search([4,5,1,2,3], 3))
print(search([2,3,4,5,1], 1))
