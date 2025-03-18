sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input("Enter your credit card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

card_number = card_number[::-1] #reverse the string

for x in card_number[::2]:
  sum_odd_digits += int(x)

for x in card_number[1::2]:
  x = int(x) * 2
  if x >= 10:
    sum_even_digits += 1 + (x % 10)
  else:
    sum_even_digits += x

total = sum_even_digits + sum_odd_digits

if total % 10 == 0:
  print("Valid")
else:
  print("Invalid")