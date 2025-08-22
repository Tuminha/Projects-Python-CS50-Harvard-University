def main():
    great_question_of_life()


def great_question_of_life():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower() #Strip here removes any leading or trailing whitespace from the input and converts it to lowercase for uniformity.
    correct_answers = ["42", "forty-two", "forty two"]
    if answer in correct_answers:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()