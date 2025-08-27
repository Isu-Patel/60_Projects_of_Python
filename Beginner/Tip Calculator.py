bill = float(input("Enter the bill amount: $"))
tip_percent = float(input("Enter tip percentage: "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount

print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount: ${total:.2f}")