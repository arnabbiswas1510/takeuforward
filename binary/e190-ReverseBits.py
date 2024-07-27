def reverseBits(n):
    res = 0
    for i in range(32):
        bit = (n >> i) & 1 #Extract the ith bit from right
        res |= bit << (31-i) #Or it (keep adding) to res after reversing (31-i)
    return res

print(reverseBits(0b11111111111111111111111111111101)) #Use 0b prefix for binary