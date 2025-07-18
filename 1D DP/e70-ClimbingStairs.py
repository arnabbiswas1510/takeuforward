"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

I didnt follow - The total number of ways to reach step n is the sum of the ways to reach:

(n - 1) steps (if you took 1 step)

(n - 2) steps (if you took 2 steps)

Ans:
Let me explain why the total number of ways to climb n steps is the sum of:

Ways to climb (n-1) steps (after taking 1 step)

Ways to climb (n-2) steps (after taking 2 steps)

1. Understanding Choices at Each Step
When you're at the bottom of a staircase with n steps, you have two options:

Take a single step (1 step)

Now you're at step 1, with (n-1) steps remaining.

Take a double step (2 steps)

Now you're at step 2, with (n-2) steps remaining.

Example:
For n = 3 (3 steps), your initial choices are:

Option 1: Take 1 step → 2 steps left.

Option 2: Take 2 steps → 1 step left.

"""
from typing import List


class SolutionTopDown:
    def climbStairs(self, n, memo=None):
        if memo is None:
            memo = {}  # Initialize memo table on first call

        # Base cases, only base cases are different from Fibonacci series
        if n == 0:
            return 1
        if n < 0:
            return 0

        # Check if already computed
        if n in memo:
            return memo[n]

        # Compute and store the result
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]

# Python3
class SolutionBottomUp:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

class SolutionConstantSpace:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second

s=SolutionTopDown()
print(s.climbStairs(n = 3))