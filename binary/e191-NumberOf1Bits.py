"""
Intuition is that since Int is 32 bits, you right shift all bits 32 times
AND the result with 1 and keep adding that to the final cnt
"""
def hammingWeight(n: int) -> int:
    res = 0

    for i in range(32):
        if (n >> i) & 1:  # 1 if the ith bit is 1
            res += 1

    return res

print()