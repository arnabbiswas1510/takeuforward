def reverseString(s: str) -> str:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]  # Swap
        left += 1
        right -= 1
    return s

print(reverseString("hello"))