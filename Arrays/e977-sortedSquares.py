"""
In this problem you need to iterate backwards on the result array. Why?
"""

def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n - 1, -1, -1): #Iterate backwards, why?
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result

print(sortedSquares([-4,-1,0,3,10]))