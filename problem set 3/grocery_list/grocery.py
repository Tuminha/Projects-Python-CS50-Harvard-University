"""
implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
Treat the user’s input case-insensitively.
"""

def main():
    grocery_list =[]
    while True:
        try:
            item = input().upper()
            grocery_list.append(item)
        except EOFError: #when the user presses control-d
            unique_items = sorted(set(grocery_list))
            for item in unique_items:
                count = grocery_list.count(item)
                print(f"{count} {item}")
            break

if __name__ == "__main__":
    main()

