num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter a operator: '+' '-' '*' '/'\n ")

if operator == "+":
  result = num1 + num2
  print(f"{num1} {operator} {num2} = {round(result,2)}")
elif operator == "-":
  result = num1 - num2
  print(f"{num1} {operator} {num2} = {round(result,2)}")
elif operator == "*":
  result = num1 * num2
  print(f"{num1} {operator} {num2} = {round(result,2)}")
elif operator == "/":
  result = num1 / num2
  print(f"{num1} {operator} {num2} = {round(result,2)}")
else:
  print(f"{operator} is not valid. Please provide a valid operator.")

