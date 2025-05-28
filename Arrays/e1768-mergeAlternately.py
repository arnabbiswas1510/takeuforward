"""
Note the fact that in this simple case you dont need to keep a flag as you would start out thinking.
Instead just let code flow handle the alternating
Also note that in this case you can simplify the if check to just do OR instead of AND.
And "".join(arr) to convert Arry to Str in Python
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)