class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        longest = ""
        #Check method below to print all substrings of a string in n^2
        n = len(s)
        for i in range(n):          # Start index
            for j in range(i, n):   # End index
                if check(i, j+1):
                    substring = s[i:j+1]
                    #Instead of the check function you can also do: if substring == substring[::-1]:
                    if len(substring) > len(longest):
                        longest = substring
        return longest

    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # Initialize DP table
        dp = [[False] * n for _ in range(n)]

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        max_len = 1
        start = 0

        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check for substrings longer than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # ending index
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_len:
                        max_len = length
                        start = i

        return s[start:start + max_len]

    def longestPalindrome3(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        ans = [0, 0]

        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i : j + 1]

s=Solution()
print(s.longestPalindrome("cdaabcbaab"))
print(s.longestPalindrome2("cbbd"))