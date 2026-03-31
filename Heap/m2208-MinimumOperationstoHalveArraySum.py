"""
Minimum Operations to Halve Array Sum (LeetCode 2208)

Problem:
You are given an array nums of positive integers. In one operation, you can choose any number 
from the array and reduce it to half of its value (rounded down). You need to find the minimum 
number of operations needed such that the sum of the array is less than or equal to half of the 
original sum.

Example:
- Input: nums = [5,19,8,1]
- Original sum = 33, target = 16.5
- Operations:
  1. Reduce 19 to 9, sum = 27
  2. Reduce 9 to 4, sum = 22
  3. Reduce 8 to 4, sum = 18
  4. Reduce 5 to 2, sum = 15
- Output: 4

Solution:
Use a max-heap to always reduce the largest element first (greedy approach).
This minimizes the number of operations needed since reducing the largest element 
gives the maximum reduction in sum.

Time Complexity: O(n log n) where n is the number of elements
Space Complexity: O(n) for the heap
"""
import heapq

class Solution:
    def halveArray(self, nums) -> int:
        target = sum(nums) / 2
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        ans = 0
        while target > 0:
            ans += 1
            x = heapq.heappop(heap)
            target += x / 2
            heapq.heappush(heap, x / 2)
        
        return ans

s = Solution()
print(s.halveArray([5,19,8,1]))