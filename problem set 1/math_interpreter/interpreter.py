# A program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.

def main():
    user_prompt = "Input your expression: "
    user_input = input(user_prompt)
    x, y, z = user_input.split(" ")
    print(calculator(x, y, z))

def calculator(x, y, z):
    if y == "+":
        return round(float(x) + float(z), 1)
    elif y == "-":
        return round(float(x) - float(z), 1)
    elif y == "*":
        return round(float(x) * float(z), 1)
    elif y == "/":
        return round(float(x) / float(z), 1)
    else:
        return "Invalid operator"
    
if __name__ == "__main__":
    main()