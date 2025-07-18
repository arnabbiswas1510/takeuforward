def findWinners(matches):
    from collections import defaultdict

    win_counts = defaultdict(int)
    loss_counts = defaultdict(int)
    players = set()

    for winner, loser in matches:
        win_counts[winner] += 1
        loss_counts[loser] += 1
        players.add(winner)
        players.add(loser)

    zero_loss = []
    one_loss = []

    for player in sorted(players):
        if loss_counts.get(player, 0) == 0:
            zero_loss.append(player)
        elif loss_counts.get(player, 0) == 1:
            one_loss.append(player)

    return [zero_loss, one_loss]