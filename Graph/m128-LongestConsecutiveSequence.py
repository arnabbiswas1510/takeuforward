"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Approaches:
1. Brute Force: Iterate through arr and for each item check if sequence starting from that item exists in arr. Return the
Global max as the longest streak. O(n^3)
2. Sort and return longest sequence O(nlogn)
3. Linear shown below but requires extra storage
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest_streak = 0
        for num in s: #Note this is not on nums
            if num-1 not in s:
                current_streak=1 #You need this here and not in outer block
                current_num = num #Use current_num instead of num to keep code cleaner
                #Complexity in not n^2 since this loop will be never executed if the prev number is in set
                while current_num+1 in nums:
                    current_num +=1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

s=Solution()
s.longestConsecutive([100,4,200,1,3,2])
