def get_airspeed_velocity_of(unladen_swallow):
  if unladen_swallow.type == "african":
    return # redacted
  elif unladen_swallow.type == "european":
    return # redacted

def fizzbuzz(num):
  if num % 15 == 0:
    print(f"{num}: fizzbuzz")
  elif num % 3 == 0:
    print(f"{num}: fizz")
  elif num % 5 == 0:
    print(f"{num}: buzz")

for i in range(1, 20):
  fizzbuzz(i)
