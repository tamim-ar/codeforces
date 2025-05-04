n = int(input())
events = list(map(int, input().split()))
police = 0
untreated_crimes = 0

for event in events:
    if event == -1:
        if police > 0:
            police -= 1
        else:
            untreated_crimes += 1
    else:
        police += event

print(untreated_crimes)
