"""
Sliding Window Median

Problem:
The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value, and the median is the mean of the two middle values.

For example:
- For arr = [1,3,1,2,0,5] and k = 3
- Output: [1.0,2.0,1.0,1.5,1.0]
  Window [1,3,1] => median = 1
  Window [3,1,2] => median = 2
  Window [1,2,0] => median = 1
  Window [2,0,5] => median = (1+2)/2 = 1.5

Hint:
The invariant of the algorithm is two heaps, small and large, each represent half of the current list. The length of
small is kept to be either n / 2 + 1 (when n is odd) or n / 2 (when n is even). The length of large is always n / 2.

This way we only need to peek the two heaps' top number to calculate median.

Solution: Two-heap approach with lazy deletion using a Counter to track active window elements.
- small: max-heap for lower half
- large: min-heap for upper half
- window: counter to track which elements are in the current window
"""
import heapq
from collections import Counter


class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap for the smaller half
        self.large = []  # min-heap for the larger half
        self.window = Counter()  # track elements in current window

    def addNum(self, num: int) -> None:
        # Push to small (max-heap)
        heapq.heappush(self.small, -num)
        # Pop from small and push to large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # Balance: if large has more elements, move one to small
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def removeNum(self, num: int) -> None:
        """Remove a number from the window (lazy deletion)"""
        self.window[num] -= 1
        if self.window[num] == 0:
            del self.window[num]
        
        # Clean up heap tops if they're not in window
        while self.small and -self.small[0] not in self.window:
            heapq.heappop(self.small)
        while self.large and self.large[0] not in self.window:
            heapq.heappop(self.large)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0


def medianSlidingWindow(nums, k):
    """
    Find the median of every sliding window of size k using two heaps with lazy deletion.
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    if not nums or k == 0:
        return []
    
    result = []
    small = []  # max-heap for the smaller half
    large = []  # min-heap for the larger half
    window = Counter()
    
    def clean_heaps():
        """Remove top elements from heaps that are not in window"""
        while small and -small[0] not in window:
            heapq.heappop(small)
        while large and large[0] not in window:
            heapq.heappop(large)
    
    def get_median():
        """Get median after cleaning heaps"""
        clean_heaps()
        
        if len(small) > len(large):
            return float(-small[0])
        else:
            return (-small[0] + large[0]) / 2.0
    
    # Initialize window with first k elements
    for i in range(k):
        # Push to small (max-heap)
        heapq.heappush(small, -nums[i])
        # Pop from small and push to large
        heapq.heappush(large, -heapq.heappop(small))
        # Balance: if large has more elements, move one to small
        if len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))
        window[nums[i]] += 1
    
    result.append(get_median())
    
    # Slide the window
    for i in range(k, len(nums)):
        # Remove the leftmost element
        left = nums[i - k]
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        
        # Add the new element
        # Push to small (max-heap)
        heapq.heappush(small, -nums[i])
        # Pop from small and push to large
        heapq.heappush(large, -heapq.heappop(small))
        # Balance: if large has more elements, move one to small
        if len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))
        window[nums[i]] += 1
        
        result.append(get_median())
    
    return result


# Test the implementation
if __name__ == "__main__":
    nums1 = [1, 3, 1, 2, 0, 5]
    k1 = 3
    print(f"Input: {nums1}, k = {k1}")
    print(f"Output: {medianSlidingWindow(nums1, k1)}")
    print()
    
    nums2 = [1]
    k2 = 1
    print(f"Input: {nums2}, k = {k2}")
    print(f"Output: {medianSlidingWindow(nums2, k2)}")
    print()
    
    nums3 = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k3 = 3
    print(f"Input: {nums3}, k = {k3}")
    print(f"Output: {medianSlidingWindow(nums3, k3)}")
