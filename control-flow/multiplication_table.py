number = int(input("Enter a number to see its multiplication table: "))

for digit in range(1, 11):
    print(f"{number} * {digit} = {number * digit}")
