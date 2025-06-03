import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 50

    for i, val in enumerate(lst):
        progress = (i + 1) / total 
        filled_length = int(progress * bar_length)
        bar = "=" * filled_length + ">" + " " * \
            (bar_length - filled_length - 1)

        print(f"\r{int(progress * 100)}%|[{bar}]| {i + 1}/{total}", end='')
        yield val


def main():
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()
