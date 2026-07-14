import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140
}

print("========== STOCK PORTFOLIO TRACKER ==========")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

portfolio = {}

n = int(input("\nHow many different stocks do you want to purchase? "))

for i in range(n):
    stock = input("Enter Stock Name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

print("\n========== PORTFOLIO SUMMARY ==========")

total = 0

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total += investment

    print(f"\nStock : {stock}")
    print(f"Price : ${price}")
    print(f"Quantity : {quantity}")
    print(f"Investment : ${investment}")

print(f"\nTotal Investment = ${total}")

with open("portfolio_report.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=========================\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(f"{stock}\n")
        file.write(f"Price : {price}\n")
        file.write(f"Quantity : {quantity}\n")
        file.write(f"Investment : {investment}\n\n")

    file.write(f"Total Investment = {total}")

with open("portfolio_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Price", "Investment"])

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        writer.writerow([stock, quantity, price, investment])

    writer.writerow(["", "", "Total", total])

print("\nPortfolio saved successfully!")
print("TXT File: portfolio_report.txt")
print("CSV File: portfolio_report.csv")