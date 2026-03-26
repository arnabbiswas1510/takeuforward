def minimumCardPickup(cards):
    last_seen = {}
    min_len = float('inf')

    for i, card in enumerate(cards):
        if card in last_seen:
            current_len = i - last_seen[card] + 1
            if current_len < min_len:
                min_len = current_len
        last_seen[card] = i  # Update the last seen index

    return min_len if min_len != float('inf') else -1