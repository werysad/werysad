investment = float(input("Enter your investment amount: "))
btc_price = float(input("Enter the current price of 1 BTC: "))

#calc
btc_amount=investment/btc_price

#output
print(f"you will get {btc_amount:.8f} BTC")
