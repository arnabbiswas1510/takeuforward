"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Hint:
The invariant of the algorithm is two heaps, small and large, each represent half of the current list. The length of
small is kept to be either n / 2 + 1 (when n is odd) or n / 2 (when n is even). The length of large is always n / 2.

This way we only need to peek the two heaps' top number to calculate median.

Any time before we add a new number, there are two scenarios, (total n numbers, k = n / 2):

(1) length of (small, large) == (k, k)
(2) length of (small, large) == (k, k + 1)
After adding the number, total (n + 1) numbers, they will become:

(1) length of (small, large) == (k, k + 1)
(2) length of (small, large) == (k + 1, k + 1)
"""
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap for the smaller half
        self.large = []  # min-heap for the larger half

    def addNum(self, num: int) -> None:
        # Push to small (max-heap)
        heapq.heappush(self.small, -num)
        # Pop from small and push to large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # Balance: if large has more elements, move one to small
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2.0

# Test the implementation
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 2.0