"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
missing from the array.
"""
class SolutionSorting:
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num

class SolutionSet:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

"""
Intuition

We can harness the fact that XOR is its own inverse to find the missing element in linear time.

Algorithm

Because we know that nums contains n numbers and that it is missing exactly one number on the range 
[0..n−1], we know that n definitely replaces the missing number in nums. Therefore, if we initialize an integer to n 
and XOR it with every index and value, we will be left with the missing number. Consider the following example 
(the values have been sorted for intuitive convenience, but need not be):

"""
class SolutionXOR:
    def missingNumber(self, nums):
        missing = len(nums) #Remember this step
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

class SolutionGaussFormula:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

def missingNumber1(arr): #n^2
    for i in range(len(arr)):
        found = 0 #You absolutely need this
        for num in arr:
            if i == num:
                found = 1
                break
        if not found:
            return i #Check little mistakes like if you should return i or num here
    return -1

print("Missing number is %d" %(missingNumber1([3,0,1])))