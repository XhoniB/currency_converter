import requests

from_currency = str(input("Enter in the currency you wold like to convert from: ").upper())

if from_currency.isdigit() or len(from_currency) != 3 or any(not c.isalnum() for c in from_currency):
    raise Exception("You have to enter a string of 3 letters, not a number or symbol.")

to_currency = str(input("Enter in the currency you would like to concert to: ").upper())

if to_currency.isdigit() or len(to_currency) != 3 or any(not c.isalnum() for c in from_currency):
    raise Exception("You have to enter a string of 3 letters, not a number or symbol.")

amount = input("Enter in the amount of money: ")

if amount != int or any(not c.isalnum() for c in amount):
    raise Exception("You have to enter an integer: ")

response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
