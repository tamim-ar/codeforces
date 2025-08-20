n = int(input())  # number of games played
s = input().strip()  # outcome string

# Count occurrences of 'A' and 'D'
anton_wins = s.count('A')
danik_wins = s.count('D')

# Compare the results and print the output
if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
