def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("Family must be a list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")
    cols = len(family[0])
    for row in family:
        if not isinstance(row, list):
            raise TypeError("Each family member must be a list")
        if len(row) != cols:
            raise ValueError(
                "All family members must have the same number of attributes")

    print(f"My shapes is :({len(family)}, {cols})")

    sliced = family[start:end]
    if sliced:
        print(f"My new shapes is :({len(sliced)}, {cols})")
    return sliced
