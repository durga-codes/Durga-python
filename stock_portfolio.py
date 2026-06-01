stocks = {
    "TCS": 3500,
    "INFY": 1500,
    "WIPRO": 500,
    "RELIANCE": 2800
}

total_value = 0

print("Stock Portfolio Tracker")
print("-----------------------")

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        value = stocks[stock_name] * quantity
        total_value += value
        print(f"Value of {stock_name}: ₹{value}")
    else:
        print("Stock not found!")

print("\nTotal Portfolio Value: ₹", total_value)