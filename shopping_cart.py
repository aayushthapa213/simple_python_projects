foods = []
prices = []
total = 0

while True:
  food = input("Enter food item ('Q' to Quit): ")
  if food.upper() == 'Q':
    break
  else:
    price = float(input("Enter it's price: Rs."))
    foods.append(food)
    prices.append(price)

print("-----Your Cart-----")
for food in foods:
  print(food, end=" ")

for price in prices:
  total += price

print(f"\nYour Total is Rs.{total:.2f}")