def getAverages(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    avgs = [-1] * n
    prefix = [0] * (n + 1)

    # Compute prefix sums
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    for i in range(n):
        left, right = i - k, i + k
        if left >= 0 and right < n:
            subarray_sum = prefix[right + 1] - prefix[left]
            avgs[i] = subarray_sum // (2 * k + 1)

    return avgs