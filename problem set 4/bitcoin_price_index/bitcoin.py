"""
implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, 
, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of 
 Bitcoins in USD to four decimal places, using , as a thousands separator.

"""
import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        number_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    bitcoin_price = get_bitcoin_price()
    cost = number_bitcoins * bitcoin_price
    print(f"${cost:,.4f}")

def get_bitcoin_price(): #Using CoinDesk API https://api.coindesk.com/v1/bpi/currentprice.json
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", timeout=5)
        response.raise_for_status() #Implement a timeout in case the user is not connected to the internet or API is down
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
        return bitcoin_price
    except requests.RequestException as e:
        sys.exit(f"Error fetching Bitcoin price: {e}")


if __name__ == "__main__":
    main()

