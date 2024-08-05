"""
Brute force: Nested loop to compare each string -  n^3 time.
Optimal (Doesnt work): Write a Comparator that uses ValidAnagram to return T or F if two strings are anagrams and sort
the entire array using this comparator. nlogn*n^2 time. This is over complex since we would change the behavior of
merge sort comparisons

Optimal: Make a copy and perform a lexicographical sort:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output strs = ["aet","aet","ant","aet","ant","abt"]

Now group Input arr based on order specified by Output above.
Smarter way to do this is to sort each item and populate the map with the key as sorted string and list of values as
value. Then return the values of the array as answer.

Cost is n*klogk time and n*k space. Method with faster time is shown below. Faster because you dont need to sort
"""
from collections import defaultdict
def groupAnagrams(strs):
    groups=defaultdict(list) #Use defaultdictionary as an alternative to putifabsent in Java
    #Note how to create a default dictionary of a list of Strings above
    for string in strs:
        cnt=[0]*26 #Num of alphabets
        for c in list(string):
            cnt[ord(c)-97]+=1
        key=""
        for num in cnt:
            key += str(num)+"#" #Do this for the boundary condition illustrated in the image
        groups[key].append(string)
    return groups.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))