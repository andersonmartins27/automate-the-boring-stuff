def plus_one(number:  int) -> int:
    return number + 1

def add(number1: int , number2: int) -> int:
    total_sum = number1
    for i in range(number2):
       total_sum = plus_one(total_sum)
    return total_sum

def multiply(number1: int, number2: int) -> int:
    total = 0
    for i in range(number2):
        total = add(total, number1)
    return total

print(add(5,3))
print(multiply(5,3))