import sys
"""
Important Note about Kadane: Note that this is n^3 and NOT n^2!!
This is because u need to keep track of ALL subarrays - Not just the incremental ones (n^2)
Note how this is done below (note the terminating condition in the k loop) 
Hint: This is a subarray of i..j where i and j are dictated by the outer loop and j starts with i
"""
def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    for i in range(n):
        for j in range(i, n):
            # subarray = arr[i.....j]
            summ = 0
            # add all the elements of subarray:
            for k in range(i, j+1):
                summ += arr[k]
            maxi = max(maxi, summ)
    return maxi

def maxSubarraySum2(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += arr[j]
            maxi = max(maxi, summ) #Remember to indent this or wrong answer, same as n^2!!
    return maxi

def maxSubarraySum3(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    summ = 0
    for i in range(n):
        summ += arr[i]
        if summ <0:
            summ = 0
        # Or the above 3 lines can be simply performed as:
        # summ = max(arr[i], summ+arr[i]) #Remember this is arr[i] on left
        maxi = max(maxi, summ) #Remember to indent this or wrong answer, same as n^2!!
    return maxi

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(arr)
    maxSum = maxSubarraySum3(arr, n)
    print("The maximum subarray sum is:", maxSum)