def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length (must be between 2 and 6 characters)
    if len(s) < 2 or len(s) > 6:
        return False
    
    # First two characters must be letters
    if not s[0:2].isalpha():
        return False
    
    # Check for valid characters and number placement
    first_number = None
    for i, char in enumerate(s):
        # Must be alphanumeric
        if not char.isalnum():
            return False
            
        # Check number placement
        if char.isdigit():
            if first_number is None:
                first_number = i
                # First number can't be '0'
                if char == '0':
                    return False
            elif i < first_number:
                return False
        elif first_number is not None and char.isalpha():
            # No letters after numbers
            return False
    
    return True

if __name__ == "__main__":
    main()
