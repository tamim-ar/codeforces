t = int(input())
for _ in range(t):
    n = int(input())
    round_numbers = []
    place = 1
    while n > 0:
        if n % 10 != 0:
            round_numbers.append(n % 10 * place)
        n //= 10
        place *= 10
    print(len(round_numbers))
    print(*round_numbers)
