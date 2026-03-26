"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window. If there is no such substring, return the empty
string "".

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Sliding window similar to

but harder
"""
from collections import Counter

def minWindow(s,t):
    if not (s and t):
        return "" #We will be returning string version of smallest window

    countT, windowCount =Counter(t), {}
    """
    Instead of Counter you can always do:
    for c in t:
        countT[c]= 1+countT.get(c, 0)
    """
    have, need = 0, len(countT) #Remember this fundamental driver for this algo
    res, resLen= [-1,-1], float("infinity")
    l=0
    for r in range(len(s)):
        c=s[r]
        windowCount[c] = 1+windowCount.get(c,0) #First update windowCount with this c
        if c in countT and countT[c] == windowCount[c]:
            have+=1 #Increase have if condition met
        while have == need: #Is condition met
            if (r-l+1) < resLen: #And is this window smaller
                res=[l,r]
                resLen=r-l+1
            #pop from left of window
            windowCount[s[l]] -=1
            if s[l] in countT and windowCount[s[l]] < countT[s[l]]: #Similar but not same as line 34
                have-=1
            l+=1
    l,r=res #Note this new style
    return s[l:r+1] if resLen !=float("infinity") else ""

print(minWindow("ADOBECODEBANC","ABC"))


