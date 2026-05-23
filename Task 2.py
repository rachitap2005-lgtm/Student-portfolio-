stocks = {"AAPL": 180, "TSLA": 250, "GOOGLE": 150}

stock = input("Enter stock name: ").upper()
qty = int(input("Enter quantity: "))

if stock in stocks:
    total = stocks[stock] * qty
    print("Total Investment =", total)
else:
    print("Stock not found")