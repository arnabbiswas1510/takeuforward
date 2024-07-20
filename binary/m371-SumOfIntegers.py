"""
Just memorize below Algo.
The carry bit has to be AND and the sum XOR without accomodating for the carry
Hence the below routine works
"""
def getSum(x, y):
    carry=None
    while(y != 0):
        #generate carry
        carry = x & y
        #xor x,y and assign the result into x
        x = x ^ y
        #left shift carry and assign into y
        y = carry << 1
    return x

print(getSum(11,19))
