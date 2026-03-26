def minStartValue(nums: list[int]) -> int:
    min_prefix = current_sum = 0
    for num in nums:
        current_sum += num
        min_prefix = min(min_prefix, current_sum)
    return max(1, 1 - min_prefix)