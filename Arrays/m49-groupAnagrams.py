from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        # Sort the string and use it as a key
        sorted_s = tuple(sorted(s))
        anagram_map[sorted_s].append(s)

    return list(anagram_map.values())