n = int(input())
scores = list(map(int, input().split()))

amazing = 0
min_score = max_score = scores[0]

for score in scores[1:]:
    if score > max_score:
        amazing += 1
        max_score = score
    elif score < min_score:
        amazing += 1
        min_score = score

print(amazing)
