import math

n = int(input())
res = n // 5

if n % 5 != 0:
    res += 1

print(res)