n = input().strip()

# Step 1: Count the lucky digits (4 and 7)
lucky_count = sum(1 for digit in n if digit in '47')

# Step 2: Check if the lucky_count is a lucky number
if all(digit in '47' for digit in str(lucky_count)):
    print("YES")
else:
    print("NO")
