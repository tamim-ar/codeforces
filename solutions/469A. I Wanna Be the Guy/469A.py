n = int(input())
x = list(map(int, input().split()))[1:]
y = list(map(int, input().split()))[1:]
passed = set(x + y)
print("I become the guy." if len(passed) == n else "Oh, my keyboard!")
