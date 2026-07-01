op = input("Enter operation (+, -, *, /): ")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
res = {"+": n1 + n2, "-": n1 - n2, "*": n1 * n2, "/": n1 / n2 if n2 != 0 else "Error"}
print("Result:", res.get(op, "Invalid Operator!"))
