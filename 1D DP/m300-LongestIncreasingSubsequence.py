"""
See visualization

Key Observations
dp[i] tracks the LIS length ending at nums[i].

Each dp[i] is updated by checking all previous elements (nums[j] where j < i).

The final answer is the maximum value in dp.
"""
class SolutionBottomUp:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

""" Approach 2: Binary Search (O(n log n) Time)*  
*Idea*: Maintain a list tails that stores the smallest possible tail value for increasing subsequences of various 
lengths. Use binary search to efficiently update this list.

*Steps*:
1. Initialize an empty list tails.
2. For each num in nums:
   - Use binary search to find the first index in tails where tails[index] >= num.
   - If found, replace tails[index] with num.
   - If not found, append num to tails.
3. The length of tails is the LIS length.

*Example*:  
For nums = [10,9,2,5,3,7,101,18]:

tails evolves as: [10] → [9] → [2] → [2,5] → [2,3] → [2,3,7] → [2,3,7,101] → [2,3,7,18]
Final length = 4

"""
import bisect
class Optimal:
    def lengthOfLIS(self, nums):
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)

s=SolutionBottomUp()
print(s.lengthOfLIS( [3, 1, 4, 2]))
print(s.lengthOfLIS( [10, 9, 2, 5, 3, 7, 101, 18]))