"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
order.

Both Heap and Quick Select methods are shown below. Bucket sort is another
"""
import collections
import heapq
import random
from typing import List

#Using Max Heap
def topKFrequent(nums, k) :
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    heap = []
    for key in hashmap:
        heapq.heappush(heap, (-hashmap[key], key)) #Python creates Min Heap by default and you want MaxHeap by key

    res = []
    for _ in range(k): #Since you just want to do it k times you dont care about having a variable
        popped = heapq.heappop(heap)
        res.append(popped[1])
    return res

from collections import Counter
#Using Quick Select
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())


        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. Move the pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. Move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. Move the pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # Select a random pivot_index
            pivot_index = random.randint(left, right)

            # Find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # If the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
                # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All elements on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]

#bucket sort O(n)
def topKFrequent3(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    n=len(nums)
    cnt=Counter(nums)
    buckets=[[] for _ in range(n)]
    for key,count in enumerate(cnt):
        buckets[count-1].append(key)
    ans=[]
    for i in range(n-1,-1,-1):
        if k-len(buckets[i])<0:
            ans+=buckets[i][:k]
            break
        else:
            ans+=buckets[i]
            k-=len(buckets[i])
    return ans
s=Solution()
print(topKFrequent3([1,1,1,2,2,3], 2))