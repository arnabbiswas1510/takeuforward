def equalPairs(grid):
    n = len(grid)
    row_counts = {}
    count = 0

    # Count each row's occurrence
    for row in grid:
        row_tuple = tuple(row)
        row_counts[row_tuple] = row_counts.get(row_tuple, 0) + 1

    # Check each column against row counts
    for j in range(n):
        column = [row[j] for row in grid] #Check this
        column_tuple = tuple(column)
        count += row_counts.get(column_tuple, 0)

    return count

print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))