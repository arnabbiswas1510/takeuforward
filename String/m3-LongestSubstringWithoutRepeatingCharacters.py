"""
Do this both with and without extra space. This question is tricky and I got it wrong because I naively deleted the set
as soon as I encountered a previous character in the input string.
"""
#Doesnt work for "dvdf"
def lengthOfLongestSubstringBad(s):
    unique=set()
    currMax,globalMax=-1,-1
    for c in s:
        if c not in unique:
            unique.add(c)
        else:
            currMax=len(unique)
            globalMax=max(globalMax,currMax)
            unique=set()
            unique.add(c)
    currMax=len(unique)
    globalMax=max(globalMax,currMax)
    return globalMax


#Note variable names str and maxAns below
#Bruteforce, same as Kadane. This is not n^3 though since we dont need the third loop for summing
def lengthOfLongestSubstring(str):
    maxAns=0
    for i in range(len(str)):
        s=set()
        for j in range(i,len(str)): #Kadane
            if str[j] in s:
                maxAns=max(maxAns,j-i) #Note where maxAns is computed
                break
            s.add(str[j])
    return maxAns

#Optimal time but still needs O(n) space
def lengthOfLongestSubstring2(str):
    maxAns=-1
    s=set()
    l=0
    for r in range(len(str)):
        while l<r and str[r] in s: #Remove everything in the string till the last occurence of this character
            s.remove(str[l]) #Remove l here and not r. Why?? (See above comment)
            l+=1
        s.add(str[r])
        maxAns=max(maxAns,r-l+1)
    return maxAns

#You can make this constant storage by using an array for 128 booleans (for all ASCII symbols)
#Still gets wrong answers in leetcode
def lengthOfLongestSubstring3(str):
    maxAns=-1
    s={}
    l=0
    for r in range(len(str)):
        if str[r] in s:
            #maxAns=max(maxAns,r-s[str[r]]-1) --This is flawed because then you will need to do it again after the loop.
            # Instead update a l pointer
            l=max(l,s[str[r]])
        s[str[r]]=r
        maxAns=max(maxAns,r-l)
    return maxAns

print(lengthOfLongestSubstring3("abcaabcdba"))

print(lengthOfLongestSubstring("aab"))