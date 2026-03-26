from collections import defaultdict

def largestUniqueNumber(nums):
    frequency = defaultdict(int)
    for num in nums:
        frequency[num] += 1

    unique_numbers = [num for num in frequency if frequency[num] == 1]

    if not unique_numbers:
        return -1
    else:
        return max(unique_numbers)