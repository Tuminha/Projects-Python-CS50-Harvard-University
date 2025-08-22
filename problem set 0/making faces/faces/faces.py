input = input("Input: ")

def convert(str):
    if str == ":)":
        return  "🙂"
    if str == ":(":
        return "🙁"
    else:
        return "😒"


def main():
    if str(input) == "Hello :)":
        print("Hello " + convert(":)"))
    elif str(input) == "Goodbye :(":
        print("Goodbye " + convert(":("))
    else:
        print("Hello " + convert(":)") + " " + "Goodbye " + convert(":("))


main()