"""implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, 
converting any codes (or aliases) therein to their corresponding emoji."""

import emoji

def main():
    user_input = input("Input: ")
    emojized = emoji.emojize(user_input, language='alias')
    print(emojized)

if __name__ == "__main__":
    main()

