t = int(input())  
s = [input().strip() for _ in range(t)]  

for word in s:
    if len(word) > 10:
        print(f"{word[0]}{len(word) - 2}{word[-1]}")
    else:
        print(word)