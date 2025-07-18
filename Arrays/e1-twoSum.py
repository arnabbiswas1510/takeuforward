def twoSum(arr, target): #Extra space
    s={}
    for i in range(len(arr)):
        if target - arr[i] in s:
            return (i, s[target-arr[i]])
        else:
            s[arr[i]]=i
    return -1

#Below solution cannot be used if we need to return indexes of the 2 numbers, since we are sorting
def twoSum2(arr, target):
    start, end = 0, len(arr)-1
    arr.sort()
    while start <= end:
        if arr[start] + arr[end] < target:
            start+=1
        elif arr[start] + arr[end] > target:
            end -=1
        else:
            return start, end
    return -1

print(twoSum([3,2,4], 6))