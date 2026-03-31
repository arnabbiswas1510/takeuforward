import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones) # turns an array into a heap in linear time
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))

        return -stones[0] if stones else 0

s=Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))