n = int(input())
heights = list(map(int, input().split()))

max_height = max(heights)
min_height = min(heights)

max_index = heights.index(max_height)
min_index = n - 1 - heights[::-1].index(min_height)

moves = max_index + (n - 1 - min_index)
if max_index > min_index:
    moves -= 1

print(moves)
