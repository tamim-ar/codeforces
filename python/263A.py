def main():
    matrix = [input().split() for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == '1':
                print(abs(i - 2) + abs(j - 2))
                return

if __name__ == "__main__":
    main()
