class Solution:
    count=0
    def countSubstrings(self, s):
        for i in range(len(s)):
            self.palindromeCount(s, i, i) #Odd combinations
            self.palindromeCount(s, i, i+1) #Even combinations
        return self.count

    def palindromeCount(self, s, i , j):
        while i>=0 and j<len(s) and s[i] == s[j]:
            self.count+=1
            i-=1
            j+=1

s=Solution()
print(s.countSubstrings("cdaabcbaab"))
