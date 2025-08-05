def currency_converter():
    rate = float(input("Enter the exchange rate from USD to EUR: "))
    dollars = float(input("Enter amount in USD: "))
    euros = dollars * rate
    print(f"{dollars} USD is equal to {euros} EUR")


currency_converter()


#OUTPUT

Enter the exchange rate from USD to EUR: 500
Enter amount in USD: 200
200.0 USD is equal to 100000.0 EUR
PS C:\Users\Janakiraman B\Downloads\Udemy Certificates\Projects\python mini projects> 
