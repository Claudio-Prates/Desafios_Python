# Solution challenge one by Jonas

num1 = int(input("Insert the first number: "))
num2 = int(input("Insert the second number: "))
if num1 > num2:
  print(f"The biggest number is: First number {num1}")
elif num2 > num1:
  print(f"The biggest number is: Second number {num2}")
else:
  print("The number are the same!")