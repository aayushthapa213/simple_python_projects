menu = {
  'popcorn' : 60,
  'kurkure' : 50,
  'lays' : 50,
  'cheese balls' : 40,
  'coke' : 70,
  'sprite' : 70
}

cart = []

total = 0

print("--------MENU--------")
for key, value in menu.items():
  print(f"{key:15}: {value:.2f}")
print("---------------------")

while True:
  choice = input("Enter your choice ('q' to quit): ").lower()
  if choice == 'q':
    break
  elif menu.get(choice) is not None:
    cart.append(choice)

print("--------YOUR ORDER--------")
for food in cart:
  total += menu.get(food)
  print(food, end=' ')

print(f"\nYour Total: Rs.{total}")

