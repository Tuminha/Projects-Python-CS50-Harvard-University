# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    tweet = str(input("What's your Tweet today? "))
    print(shorten(tweet))

def shorten(tweet):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowels:
        tweet = tweet.replace(vowel, "")
    return tweet

if __name__ == "__main__":
    main()