temp = float(input("Enter the temperature: "))
unit = input("Enter the unit: 'C' for Celsius and 'F' for Fahrenheit\t")

if unit == 'C':
  result = round(( 9 * temp )/ 5+ 32, 2)
  print(f"The temperature is {result} in Fahrenheit.")
elif unit == 'F':
  result = round(( temp - 32 ) * 5 / 9, 2)
  print(f"The temperature is {result} in Celsius.")
else:
  print(f"{unit} is invalid unit!")