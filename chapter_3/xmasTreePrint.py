from random import randint

size = int(input("Enter the tree size: "))

for row_num in range(1,size+1):
    row = ""
    row += " " * (size-row_num)
    for i in range(row_num * 2 - 1):
        if randint(1, 4) == 1:
            row += "o"
        else:
            row += "^"
    print(row)
for i in range(2):
    print(f"{" " * (size-1)}#")