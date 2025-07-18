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

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        # Initialize a DP table (n x n) where dp[i][j] = True if s[i..j] is a palindrome
        dp = [[False] * n for _ in range(n)]
        start = 0      # Starting index of the longest palindrome
        max_len = 1     # Length of the longest palindrome (minimum is 1 for single characters)

        # Every single character is a palindrome (base case)
        for i in range(n):
            dp[i][i] = True

        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check for substrings of length >= 3
        for length in range(3, n + 1):          # length of substring
            for i in range(n - length + 1):     # starting index
                j = i + length - 1              # ending index
                # Check if the outer characters match and the inner substring is a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_len:
                        start = i
                        max_len = length

        return s[start:start + max_len]

    def longestPalindrome3(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = ""

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # Check if substring is palindrome
                dp[i][j] = (s[i] == s[j]) and (j-i < 2 or dp[i+1][j-1])
                if dp[i][j] and (j-i+1) > len(res):
                    res = s[i:j+1]
        return res

    def longestPalindrome4(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # Return valid palindrome

        res = ""
        for i in range(len(s)):
            res = max(res, expand(i, i), expand(i, i+1), key=len)
        return res

s=Solution()
print(s.longestPalindrome3("cdaabcbaab"))
print(s.longestPalindrome2("cbbd"))