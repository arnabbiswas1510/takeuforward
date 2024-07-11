import sys
"""
Important Note about Kadane: Note that this is n^3 and NOT n^2!!
This is because u need to keep track of ALL subarrays - Not just the incremental ones (n^2)
Note how this is done below (note the terminating condition in the k loop) 
Hint: This is a subarray of i..j where i and j are dictated by the outer loop and j starts with i
"""
def maxProductSubarray(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    for i in range(n):
        for j in range(i, n):
            # subarray = arr[i.....j]
            product = 1
            # add all the elements of subarray:
            for k in range(i, j+1):
                product *= arr[k]
            maxi = max(maxi, product)
    return maxi

def maxProductSubarray2(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            maxi = max(maxi, product) #Remember to indent this or wrong answer, same as n^2!!
    return maxi

#Memorize below method
"""
Idea is that pre and suff are around 0 since that will always break the subarray
Then you just find the max of these subarrays demarcated by the zeros
"""
def maxProductSubarray3(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    pre, suff = 1, 1
    product = 1
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= arr[i]
        suff *= arr[n-i-1]
        maxi = max(maxi, max(pre,suff))
    return maxi

if __name__ == "__main__":
    arr = [1, 2, -3, 0, -4, -5]
    n = len(arr)
    maxSum = maxProductSubarray3(arr, n)
    print("The maximum subarray product is:", maxSum)