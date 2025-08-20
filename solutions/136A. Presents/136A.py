n = int(input())
p = list(map(int, input().split()))
res = [0] * n
for i in range(n):
    res[p[i] - 1] = i + 1
print(*res)
