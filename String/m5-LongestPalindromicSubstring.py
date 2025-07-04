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
        dp = [[False]*n for _ in range(n)]
        res = ""

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # Check if substring is palindrome
                dp[i][j] = (s[i] == s[j]) and (j-i < 2 or dp[i+1][j-1])
                if dp[i][j] and (j-i+1) > len(res):
                    res = s[i:j+1]
        return res

    def longestPalindrome3(self, s: str) -> str:
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