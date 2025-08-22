"""
implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list below:
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
            elif "," in date:
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                month = convert_month_to_number(month)
            else:
                raise ValueError
            
            day = int(day)
            year = int(year)
            
            if month > 12 or month < 1 or day > 31 or day < 1:
                raise ValueError
            
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        except ValueError:
            pass

def convert_month_to_number(month):
    return months.index(month) + 1

if __name__ == "__main__":
    main()
