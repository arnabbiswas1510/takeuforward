"""
Simple but important method for Prefix Sum - repeatable
"""
def runningSum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums