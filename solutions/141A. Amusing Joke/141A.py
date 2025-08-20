from collections import Counter

# Input the guest's name, host's name, and the pile of letters
guest_name = input().strip()
host_name = input().strip()
pile = input().strip()

# Combine guest's and host's names
combined_names = guest_name + host_name

# Check if the letter counts are the same
if Counter(combined_names) == Counter(pile):
    print("YES")
else:
    print("NO")
