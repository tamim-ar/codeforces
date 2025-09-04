n, k, l, c, d, p, nl, np = map(int, input().split())

total_drink = k * l // nl
total_limes = c * d
total_salt = p // np

print(min(total_drink, total_limes, total_salt) // n)
