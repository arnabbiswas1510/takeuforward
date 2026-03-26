def findMaxLength(nums):
    max_len = 0
    balance = 0  # Represents the running difference between 1s and 0s
    balance_map = {0: -1}  # Stores the first encountered index for each balance value

    for i, num in enumerate(nums):
        if num == 1:
            balance += 1
        else:  # num == 0
            balance -= 1

        if balance in balance_map:
            max_len = max(max_len, i - balance_map[balance])
        else:
            balance_map[balance] = i

    return max_len

