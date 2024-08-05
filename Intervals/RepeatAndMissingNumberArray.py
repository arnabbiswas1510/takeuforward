"""
Problem:You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.

Brute force: Iterate through first n natural numbers and check how many times it exists in array (by scanning entire
array). If it exists more than once or not at all that's the answer. N^2 cost

Better: Use hashing with an array of size n and increment the ith index as u iterate through input array.
Then iterate through hash and return the keys with values 0 and 2. n time n space.

Optimal: Mathematical and XOR below

https://github.com/arnabbiswas1510/takeuforward/blob/a2d2a840ea456d61dc0b68e9961efe34a91f83dd/images/Intervals/RepeatAndMissingNumberArray.png
"""

#Math method, see image for explanation
def missingAndRepeatedNumber1(arr):
    totalArr, totalArrSq = 0, 0
    for num in arr:
        totalArr += num
        totalArrSq += num**2 #Remember exponentiation is ** and not ^ (which is xor)
    n= len(arr)
    totalNatural = (n*(n+1))/2
    totalNaturalSq = (n*(n+1)*(2*n+1))/6
    v1 = totalArr - totalNatural
    v2 = totalArrSq - totalNaturalSq
    repeat=(v2/v1 - v1)/2
    missing = repeat + v1
    return repeat, missing

""" XOR Method
Very involved, see steps and comments below
r,m=repeating, missing
"""
#TODO buggy
def missingAndRepeatedNumber2(arr):
    xor=0
    #Firxt xor with all elements in arr and first n numbers to get r^m
    for i in range(len(arr)):
        xor ^=arr[i]
        xor ^=i+1 #You can do this in the same loop
    #Now xor=r^m. Since r and m are 2 different numbers, they have to differ in at least one bit
    #Next we identify this right most differing bit position
    bitPos=0
    while True:
        #For such & comparisons below remember to do != 0 and not == 1. Since in the Evaluate 4 & 4 = 4 (and not 1)
        if (xor & (1 << bitPos)) != 0:#This will happen only when bitPos is 1 in xor
            break
        bitPos+=1
    #Now segregate all numbers from arr and 1..n into 2 groups -
    #Those whose bitPos is set (one) and where it is not set(zero)
    #And xor all numbers in both these groups
    zero, one = 0, 0
    for i in range(len(arr)):
        if arr[i] & (1 << bitPos) != 0:
            one ^= arr[i]
        else:
            zero ^= arr[i]
        if i & (1 << bitPos) != 0:
            one ^= i
        else:
            zero ^= i
    #See explanation if needed but understand that doing the xor like this in two groups cancelled all but the odd no.
    # of repeating elements and hence zero and one will finally be m and r
    # But we dont yet know which is which. So..
    cnt=0
    for num in arr:
        if num == zero:
            cnt+=1
    if cnt == 2:
        return zero, one
    return one, zero

print(missingAndRepeatedNumber2([4,3,6,2,1,1]))