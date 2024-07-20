"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
missing from the array.
"""

def missingNumber1(arr): #n^2
    for i in range(len(arr)):
        found = 0 #You absolutely need this
        for num in arr:
            if i == num:
                found = 1
                break
        if not found:
            return i #Check little mistakes like if you should return i or num here
    return -1

def missingNumber1(arr): #n^2
    for i in range(len(arr)):
        found = 0 #You absolutely need this
        for num in arr:
            if i == num:
                found = 1
                break
        if not found:
            return i #Check little mistakes like if you should return i or num here
    return -1

print("Missing number is %d" %(missingNumber1([3,0,1])))