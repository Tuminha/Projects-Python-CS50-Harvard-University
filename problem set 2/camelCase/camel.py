# Problem: program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
def main():
    input_camel = input("Input here the camelCase variable:  ")
    print(camel_to_snake(input_camel))

def camel_to_snake(input_camel):
    snake_case = ""
    for char in input_camel:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()