num1 = int(input("enter first number "))
num2 = int(input("enter second number "))
opt = input("enter operator ")

result = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b 
}[opt](num1, num2)

print(result)