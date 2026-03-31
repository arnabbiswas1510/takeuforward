"""
Remove Stones to Minimize the Total

Problem:
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile,
and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile multiple times.

Return the minimum possible total number of stones remaining after applying the k operations.

Example:
Input: piles = [5,4,9], k = 2
Output: 12
Explanation: 
Step 1: Apply operation on pile 2 (9), floor(9/2) = 4, so 9 - 4 = 5, piles = [5,4,5]
Step 2: Apply operation on pile 0 (5), floor(5/2) = 2, so 5 - 2 = 3, piles = [3,4,5]
Total = 3 + 4 + 5 = 12

Solution: Use a max-heap to always operate on the largest pile.
Time Complexity: O(k log n)
Space Complexity: O(n)
"""
import heapq

def minStoneSum(piles, k):
    """
    Minimize the total stones by removing floor(pile/2) from the largest pile k times.
    """
    # Create max-heap using negative values
    max_heap = [-pile for pile in piles]
    heapq.heapify(max_heap)
    
    for _ in range(k):
        # Get the largest pile (most negative)
        largest = -heapq.heappop(max_heap)
        # Remove floor(largest / 2) stones
        remove = largest // 2
        new_size = largest - remove
        # Push back the new size
        heapq.heappush(max_heap, -new_size)
    
    # Calculate total remaining stones
    total = sum(-pile for pile in max_heap)
    return total

# Test the implementation
if __name__ == "__main__":
    # Test case 1
    piles1 = [5, 4, 9]
    k1 = 2
    print(f"Input: piles = {piles1}, k = {k1}")
    print(f"Output: {minStoneSum(piles1, k1)}")
    print()
    
    # Test case 2
    piles2 = [4, 3, 6, 7]
    k2 = 3
    print(f"Input: piles = {piles2}, k = {k2}")
    print(f"Output: {minStoneSum(piles2, k2)}")
    print()
    
    # Test case 3
    piles3 = [1]
    k3 = 1
    print(f"Input: piles = {piles3}, k = {k3}")
    print(f"Output: {minStoneSum(piles3, k3)}")
