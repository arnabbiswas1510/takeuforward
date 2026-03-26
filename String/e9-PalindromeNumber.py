"""
What this question checks is the ability to extract the MSB and LSB of the number in each iteration (no turning the
number to a string). But it's difficult to extract MSB. Hence build reverse num instead as shown below and proceed
"""

def palindrome(n):
    revN=0
    dup=n #Save n
    while n >0:
        lsb=n%10
        revN=10*revN + lsb
        n//=10
    return dup == revN

print(palindrome(4555))
