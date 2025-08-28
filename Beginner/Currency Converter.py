rates = {
    "USD": {"EUR": 0.85, "GBP": 0.75, "JPY": 110},
    "EUR": {"USD": 1.18, "GBP": 0.88, "JPY": 129},
    "GBP": {"USD": 1.33, "EUR": 1.14, "JPY": 147}
}

from_currency = input("From currency (USD/EUR/GBP): ").upper()
to_currency = input("To currency (USD/EUR/GBP): ").upper()
amount = float(input("Enter amount: "))

if from_currency == to_currency:
    converted = amount
else:
    converted = amount * rates[from_currency][to_currency]

print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")