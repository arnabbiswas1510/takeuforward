from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10

            return digit_sum

        dic = defaultdict(list)
        for num in nums:
            digit_sum = get_digit_sum(num)
            dic[digit_sum].append(num)

        ans = -1
        for key in dic:
            curr = dic[key]
            if len(curr) > 1:
                curr.sort(reverse=True)
                ans = max(ans, curr[0] + curr[1])

        return ans