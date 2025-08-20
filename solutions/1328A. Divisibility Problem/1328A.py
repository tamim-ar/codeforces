t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    remainder = a % b
    print(0 if remainder == 0 else b - remainder)
