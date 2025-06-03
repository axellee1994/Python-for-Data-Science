import sys
from ft_filter import ft_filter


def main():
    """
    Main function to filter words based on length
    from command line arguments.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = text.split()
        result = ft_filter(lambda x: len(x) > n, words)
        print(list(result))

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
