print("                                                                                                 Calculator                          \n")
print("                                                                         ")

num1 = float(input("Please enter your first number: "))
op = input("Please enter your operator(+ or - or / or *): ")
num2 = float(input("Please enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid expression. Read instructions carefully.")