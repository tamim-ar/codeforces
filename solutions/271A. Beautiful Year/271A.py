y = int(input())

def has_unique_digits(year):
    return len(set(str(year))) == 4

y += 1
while not has_unique_digits(y):
    y += 1

print(y)
