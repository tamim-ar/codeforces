n = int(input())
current = 0
max_passengers = 0

for _ in range(n):
    a, b = map(int, input().split())
    current -= a
    current += b
    if current > max_passengers:
        max_passengers = current

print(max_passengers)
