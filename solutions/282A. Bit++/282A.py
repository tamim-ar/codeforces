def main():
    x = 0
    n = int(input())
    for _ in range(n):
        operation = input().strip()
        if operation == "++X" or operation == "X++":
            x += 1
        elif operation == "--X" or operation == "X--":
            x -= 1
    print(x)

if __name__ == "__main__":
    main()
