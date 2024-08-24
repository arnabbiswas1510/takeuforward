""""
Brute force: Add both the Strings to a list and then iterate thru first one and check for the existence of that
character in the second list. If it exists, remove from that list
At the end if all characters exist and the second list is empty return True, else False. n^2

Better: Sort both strings and check for equality - nlogn

Even Better: Hashmap with each character as key and count as value. Similar to Brute force but you keep reducing count
This will be n
"""
def isAnargram(s1,s2):
    counter = [0]*26 #Since contains only lowercase letters
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        counter[ord(s1[i])-97]+=1
        counter[ord(s2[i])-97]-=1 #increment and decrement in same loop
    for i in range(26):
        if counter[i] != 0:
            return False
    return True

print(isAnargram("anagram","nagaram"))
print(isAnargram("rat","car"))