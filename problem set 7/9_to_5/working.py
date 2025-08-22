import re
import sys

def main():
    print(convert(input("Hour to convert: ")))

def convert(hour: str):
    # Check if the input has the "to" format
    if " to " in hour:
        # Split the input into start and end times
        start_time, end_time = hour.split(" to ")
        
        # Convert each time separately
        start_24h = convert_single_time(start_time.strip())
        end_24h = convert_single_time(end_time.strip())
        
        # Return the combined result
        return f"{start_24h} to {end_24h}"
    else:
        # Handle single time input
        return convert_single_time(hour)

def convert_single_time(time_str: str):
    # Check if the time comes in american format (12 hours) in different formats like 9 AM or 9:00 AM
    if re.search(r"^(\d{1,2}):(\d{1,2}) (AM|PM)$", time_str):
        match = re.search(r"^(\d{1,2}):(\d{1,2}) (AM|PM)$", time_str)
        hours = int(match.group(1))
        minutes = int(match.group(2))
        am_pm = match.group(3)
        
        # CRITICAL: Validate hours and minutes BEFORE any processing
        if hours < 1 or hours > 12:
            raise ValueError("Invalid hour")
        if minutes < 0 or minutes > 59:
            raise ValueError("Invalid minutes")
            
    elif re.search(r"^(\d{1,2}) (AM|PM)$", time_str):
        # Handle format like "9 AM" (without minutes)
        match = re.search(r"^(\d{1,2}) (AM|PM)$", time_str)
        hours = int(match.group(1))
        minutes = 0
        am_pm = match.group(2)
        
        # Validate hours
        if hours < 1 or hours > 12:
            raise ValueError("Invalid hour")
    else:
        raise ValueError("Invalid time format")
    
    # Convert to 24-hour format
    if am_pm == "AM":
        if hours == 12:
            hours = 0
        return f"{hours:02d}:{minutes:02d}"
    elif am_pm == "PM":
        if hours == 12:
            hours = 12
        else:
            hours += 12
        return f"{hours:02d}:{minutes:02d}"
    else:
        raise ValueError("Invalid AM/PM")

if __name__ == "__main__":
    main()