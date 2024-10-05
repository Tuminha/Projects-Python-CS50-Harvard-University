# Problem statement:
"""
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, 
and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
"""

def main():
    time = input("What time is it? ")
    float_time = convert(time)
    print(meal_time(float_time))

def convert(time):
    if ":" in time:
        hours, minutes = time.split(":")
        if "a.m." in minutes.lower() or "p.m." in minutes.lower():
            period = minutes[-4:].lower()
            minutes = minutes[:-5]
            hours = float(hours)
            if period == "p.m." and hours != 12:
                hours += 12
            elif period == "a.m." and hours == 12:
                hours = 0
        else:
            hours = float(hours)
            minutes = float(minutes)
    else:
        hours = float(time)
        minutes = 0
    
    return hours + minutes / 60

def meal_time(time):
    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"
    else:
        return ""

if __name__ == "__main__":
    main()