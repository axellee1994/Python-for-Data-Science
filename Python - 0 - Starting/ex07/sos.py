import sys

NESTED_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", " ": "/"
}


def morse_code(text):
    """Converts text to Morse code."""
    morse = []
    for char in text.upper():
        if char in NESTED_MORSE:
            morse.append(NESTED_MORSE[char])
    return " ".join(morse)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        for char in sys.argv[1]:
            if char.upper() not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")

        result = morse_code(sys.argv[1])
        print(result)

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
