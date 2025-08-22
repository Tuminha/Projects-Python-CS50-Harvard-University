import re
import sys

# A function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not
# Example of a IPv4 address: 127.0.0.1

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = re.compile(
        r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d?|0)\.'
        r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d?|0)\.'
        r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d?|0)\.'
        r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d?|0)$'
    )
    return bool(pattern.match(ip))

if __name__ == "__main__":
    main()