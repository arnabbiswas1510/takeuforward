"""
Note that the below method does **NOT** work
Use sort or Set method instead
"""
def containsDuplicate(arr):
    for num in arr:
        if arr[num] < 0:
            return True
        else:
            arr[num] = -arr[num]
    return False

print(containsDuplicate([1, 2, 3, 4]))