from collections import Counter

def max_instances_of_balloon(text):
    count = Counter(text)
    return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])