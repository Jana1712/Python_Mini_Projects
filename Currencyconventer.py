def currency_converter():
    rate = float(input("Enter the exchange rate from USD to EUR: "))
    dollars = float(input("Enter amount in USD: "))
    euros = dollars * rate
    print(f"{dollars} USD is equal to {euros} EUR")

currency_converter()