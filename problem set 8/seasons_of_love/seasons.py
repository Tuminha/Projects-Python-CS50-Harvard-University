from datetime import date
import sys

def main():
    birth_date = input("Date of birth: ")
    # If is not in YYYY-MM-DD format exit via sys.exit
    if not birth_date:
        sys.exit("Invalid date")
    try:
        birth_date = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date")
    date_today = date.today()
    days_since_birth = (date_today - birth_date).days
    minutes_since_birth = days_since_birth * 24 * 60
    
    # Convert minutes to words
    minutes_in_words = convert_number_to_words(minutes_since_birth)
    print(f"{minutes_in_words} minutes")

def convert_number_to_words(number):
    """Convert a number to its English word representation"""
    if number == 0:
        return "Zero"
    
    # Handle numbers up to millions
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    def convert_hundreds(n):
        result = ""
        if n >= 100:
            result += ones[n // 100] + " hundred"
            n %= 100
            if n > 0:
                result += " "
        
        if n >= 20:
            result += tens[n // 10]
            if n % 10 > 0:
                result += "-" + ones[n % 10]
        elif n > 0:
            result += ones[n]
        
        return result
    
    def convert_number(n):
        if n == 0:
            return ""
        
        result = ""
        
        # Millions
        if n >= 1000000:
            millions = n // 1000000
            result += convert_hundreds(millions) + " million"
            n %= 1000000
            if n > 0:
                result += ", "
        
        # Thousands
        if n >= 1000:
            thousands = n // 1000
            result += convert_hundreds(thousands) + " thousand"
            n %= 1000
            if n > 0:
                result += ", "
        
        # Hundreds
        if n > 0:
            result += convert_hundreds(n)
        
        return result
    
    words = convert_number(number)
    # Capitalize first letter
    return words[0].upper() + words[1:] if words else ""

if __name__ == "__main__":
    main()