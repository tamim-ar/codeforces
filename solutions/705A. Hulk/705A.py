n = int(input())
result = []

for i in range(1, n + 1):
    if i % 2 == 1:
        result.append("I hate")
    else:
        result.append("I love")
    if i != n:
        result.append("that")
    else:
        result.append("it")

print(" ".join(result))
