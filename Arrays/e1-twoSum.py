def twoSum(arr, target): #Extra space
    s={}
    for i in range(len(arr)):
        if target - arr[i] in s:
            return (arr[i], target-arr[i])
        else:
            s[arr[i]]=i
    return -1

def twoSum2(arr, target):
    start, end = 0, len(arr)-1
    arr.sort()
    while start <= end:
        if arr[start] + arr[end] < target:
            start+=1
        elif arr[start] + arr[end] > target:
            end -=1
        else:
            return arr[start], arr[end]
    return -1

print(twoSum2([2,6,5,8,11], 14))