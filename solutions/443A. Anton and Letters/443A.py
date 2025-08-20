s = input()
s = s[1:-1]  # remove the curly brackets

if s.strip() == "":
    print(0)
else:
    letters = set(s.replace(",", "").split())
    print(len(letters))
