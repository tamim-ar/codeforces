s = input()
if sum(1 for c in s if c.isupper()) > len(s) // 2:
    print(s.upper())
else:
    print(s.lower())
