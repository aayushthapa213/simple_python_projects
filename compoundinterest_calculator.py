principle = 0
rate = 0
time = 0

while principle <= 0:
  principle = float(input("Enter the principle amount: "))
  if principle <= 0:
    print("Principle must be greater than 0!")
  
while rate <= 0:
  rate = float(input("Enter the rate: "))
  if rate <= 0:
    print("Rate must be greater than 0!")

while time <= 0:
  time = float(input("Enter the time: "))
  if time <= 0:
    print("time must be greater than 0!")

total = principle * pow( (1 + rate / 100) , time) 

print(f"Principle: {principle:.2f}")
print(f"Rate: {rate:.2f}")
print(f"Time: {time:.2f}")
print(f"Total: {total:.2f}")
