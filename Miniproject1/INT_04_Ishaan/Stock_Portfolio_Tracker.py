stock_names = []
buy_prices = []
quantities = []
current_prices = []

def add_stock():
    name = input("Enter stock name: ")
    buy_price = float(input("Enter buy price: "))
    quantity = int(input("Enter quantity: "))

    current_price = buy_price + (buy_price * 0.1) 

    stock_names.append(name)
    buy_prices.append(buy_price)
    quantities.append(quantity)
    current_prices.append(current_price)

    print("Stock added successfully!\n")

def view_portfolio():
    if len(stock_names) == 0:
        print("No stocks added yet.\n")
        return

    total_investment = 0
    total_current_value = 0

    for i in range(len(stock_names)):
        investment = buy_prices[i] * quantities[i]
        current_value = current_prices[i] * quantities[i]
        profit_loss = current_value - investment

        if investment != 0:
            profit_loss_percent = (profit_loss / investment) * 100
        else:
            profit_loss_percent = 0
        total_investment += investment
        total_current_value += current_value

        print("\nStock:", stock_names[i])
        print("Buy Price:", buy_prices[i])
        print("Current Price:", current_prices[i])
        print("Quantity:", quantities[i])
        print("Investment:", investment)
        print("Current Value:", current_value)
        print("Profit/Loss:", profit_loss)

    print("\nTotal Investment:", total_investment)
    print("Total Current Value:", total_current_value)
    print("Profit/Loss:", f"{profit_loss:+.2f}")
    print("Profit/Loss %:", f"{profit_loss_percent:+.2f} %")
 
while True:
    print("==== STOCK TRACKER ====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_stock()
    elif choice == "2":
        view_portfolio()
    elif choice == "3":
        print("Thank you for Calling Portfolio Tracker")
        break
    else:
        print("Invalid Input")