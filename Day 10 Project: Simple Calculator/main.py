# Print calculator logo
from art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for i in operations:
    print(i)

  calculator_is_on = True
  while calculator_is_on:
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = operations[operation](num1,num2)
    print(f"{num1} {operation} {num2} = {result}")

    if input(f"Type 'y' to continue calculating with {result},\nor type 'n' start a new calculation: ") == "y":
      num1 = result
    else:
      calculator_is_on = False
      calculator()

calculator()
