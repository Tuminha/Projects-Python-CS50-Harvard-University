"""
implement a program that enables a user to place an order, prompting them for items, one per line, 
until the user inputs control-d (which is a common way of ending one’s input to a program). 
After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased
"""

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    while True:
        try:
            item = input("Item: ").title() #title is to make the input case insensitive
            if item in menu:
                total += menu[item]
                print(f"${total:.2f}")
            else:
                pass
        except EOFError:
            break

if __name__ == "__main__":
    main()
