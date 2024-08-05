""""
Brute force: Add both the Strings to a list and then iterate thru first one and check for the existence of that
character in the second list. If it exists, remove from that list
At the end if all characters exist and the second list is empty return True, else False. n^2

Better: Sort both strings and check for equality - nlogn

Even Better: Hashmap with each character as key and count as value. Similar to Brute force but you keep reducing count
This will be n
"""