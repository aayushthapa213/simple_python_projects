weight = float(input("Enter your weight: "))
unit = input("Enter the unit: 'K' for Kilograms and 'P' for Pounds\t")
if unit == 'K':
  result = weight * 2.205
  print(f"Your weight is {round(result,2)} pounds.")
elif unit == 'P':
  result = weight / 2.205
  print(f"Your weight is {round(result,2)} kilograms.")
else: 
  print(f"{unit} is invalid.")