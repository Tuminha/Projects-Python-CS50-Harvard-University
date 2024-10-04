"""
In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” 
Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: 
“You got a greeting that starts with an ‘h,’ how does $20 sound?” 
"""

def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h") and greeting != "hello":
        return "$20"
    else:
        return "$100"
        
if __name__ == "__main__":
    main()