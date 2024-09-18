"""
Sliding window technique. Crus of this problem is understanding the while loop which computes minimum number of
characters to be replaced.
"""

#Below algo is O(26*n) which is O(n)
def characterReplacement(s, k):
    count={}
    res=0
    l=0
    for r in range(len(s)):
        count[s[r]]=1+count.get(s[r],0) #Or use defaultdict(int) here
        while (r-l+1)-max(count.values()) > k: #Min values to be replaced = len of window - count of most frequent letter
            count[s[l]] -=1
            l+=1
        res=max(res, r-l+1)
    return res

#Slight tweak to make this strictly O(n)
def characterReplacement2(s, k):
    count={}
    res=0
    l=0
    maxf=0
    for r in range(len(s)):
        count[s[r]]=1+count.get(s[r],0) #Or use defaultdict(int) here
        maxf=max(maxf,count[s[r]])
        while (r-l+1)-maxf > k: #Optimization is here because we dont need to counter to get max values
            count[s[l]] -=1
            l+=1
        res=max(res, r-l+1)
    return res

print(characterReplacement("AABABBA",1))