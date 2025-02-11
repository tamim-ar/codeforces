num = int(input())
count = 0

for i in range(num):
    x = input()

    if x.count("++"):
        count = int(count) + 1
    elif x.count("--"):
        count = int(count) - 1

print(count)
