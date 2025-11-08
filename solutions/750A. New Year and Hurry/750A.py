n, k = map(int, input().split())
time_left = 240 - k
solved = 0
time_spent = 0

for i in range(1, n + 1):
    time_spent += 5 * i
    if time_spent <= time_left:
        solved += 1
    else:
        break

print(solved)
