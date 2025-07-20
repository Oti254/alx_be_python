size = int(input("Enter the size of the pattern: "))

column = 0;
while column < size:
    for row in range(size):
        print(f"*", end="")
    print(f"")
    column += 1
