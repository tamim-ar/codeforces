num = int(input())

for i in range(num):
    word = input()
    if len(word) > 10:
        count = len(word)
        count1 = int(count)-2
        print(word[0]+str(count1)+word[count-1])
    else:
        print(word)