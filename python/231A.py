num = int(input())
count = 0

for i in range(num):
    x = input().split(" ")
    a, b, c = int(x[0]), int(x[1]), int(x[2])
    if a + b + c >= 2:
        count = count + 1

if count >= 2:
    print(count)
else:
    print(count)
