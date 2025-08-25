n1 = int(input("Enter the first number for using the Calculator Function: "))
n2 = int(input("Enter the second number for using the Calculator Function: "))

print('''These are the Functions you can use in this Calculator:
      1. Addition: +
      2. Subtraction: -
      3. Multiplication: *
      4. Division: /
      ''')
function_to_do = input("Enter the Symbol of the Functions given above: ")

if function_to_do == "+":
    sum = n1 + n2
    print(f"The sum of the two numbers is {sum}")
elif function_to_do == "-":
    subtraction = n1 - n2
    print(f"The subtraction of the two numbers is {subtraction}")
elif function_to_do == "*":
    multiplication = n1 * n2
    print(f"The multiplication of the two numbers is {multiplication}")
elif function_to_do == "/":
    division = n1 / n2
    print(f"The Division of the two numbers is {division}")
else: 
    print("Invalid Function. Choose only according to the Functions given above.\n")