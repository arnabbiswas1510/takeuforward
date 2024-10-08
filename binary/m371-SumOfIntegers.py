"""
Given two integers a and b, return the sum of the two integers without using the operators + and -

Just memorize below Algo.
The carry bit has to be AND and the sum XOR without accomodating for the carry
Hence the below routine works
"""
def getSum(x, y):
    carry=None
    while(y != 0):
        #generate carry
        carry = x & y #If both bits are 1 then carry is 1, hence AND
        #xor x,y and assign the result into x
        x = x ^ y #If both bits are 1 then sum is 0 (hence XOR) with carry 1
        #left shift carry and assign into y
        y = carry << 1
        #In above remember that sum is assigned to X and carry rotated left to Y
    return x

print(getSum(11,19))
