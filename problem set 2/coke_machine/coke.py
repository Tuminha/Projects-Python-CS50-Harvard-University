"""
implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

def main():
    amount_due = 50
    amount_inserted = 0

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        
        if coin in [25, 10, 5]:
            amount_inserted += coin
            amount_due -= coin
        else:
            print("Amount due: ", amount_due)
            continue
        
    
    change = abs(amount_due)
    if change >= 0:
        print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()  
