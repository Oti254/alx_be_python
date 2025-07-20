size = int(input("Enter the size of the pattern: "))

column = 0;
while column < size:
    for row in range(size):
        print("*", end="")
    print("\n")
    column += 1
