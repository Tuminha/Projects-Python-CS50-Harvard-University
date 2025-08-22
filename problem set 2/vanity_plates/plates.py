#Problem:
"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""
import re

def main():
    your_plate = input("Plese, introduce your proposed plate: ")
    if check_plate(your_plate) and check_plate_2(your_plate):
        print("Valid")
    else:
        print("Invalid")


def check_plate(plate):
    if plate[0:2].isalpha() and len(plate) >= 2 and len(plate) <= 6:
        return True
    else:
        return False

def check_plate_2(plate):
    pattern = r'^[A-Za-z]+([1-9][0-9]*)?$'
    return bool(re.match(pattern, plate))


if __name__ == "__main__":
    main()
