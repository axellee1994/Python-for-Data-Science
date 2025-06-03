import sys
import string

def character_count(text):
    """Counts the number of uppercase letters, lowercase letters

    Prints the following counts:
    1. Total characters
    2. Uppercase letters
    3. Lowercase letters
    4. Punctuation characters
    5. Spaces
    6. Digits

    """

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    spaces_count = 0
    digits_count = 0
    total = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            spaces_count += 1
        elif char.isdigit():
            digits_count += 1
        elif char in string.punctuation:
            punctuation_count += 1

    total = len(text)

    print(f"The text contains: {total} characters")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation characters")
    print(f"{spaces_count} spaces")
    print(f"{digits_count} digits")


def main():
    """Main function to read text from standard input and count characters."""

    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    elif len(sys.argv) > 2:
        raise AssertionError("Too many arguments provided.")
    else:
        text = sys.argv[1]
    
    character_count(text)

if __name__ == "__main__":
    main()
