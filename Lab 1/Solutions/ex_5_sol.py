def f5_1(filename: str) -> None:
    """
    Reads a file line by line and processes each line using split method.
    """
    with open(filename) as file:
        for line in file:
            name, count = line.split(",")
            print(int(count) * 1000, "people named", name)


def f5_2(filename: str) -> None:
    """
    Reads a file line by line and processes each line using regular expressions.
    """
    import re
    pattern = re.compile(r"([^,]+),(\d+)")
    with open(filename) as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                name, count = match.groups()
                print(int(count) * 1000, "people named", name)


def f5_3(filename: str) -> None:
    """
    Implements error handling with try-except for robust parsing.
    """
    with open(filename) as file:
        for line in file:
            try:
                name, count = line.strip().split(",")
                print(int(count) * 1000, "people named", name)
            except ValueError:
                continue


def f5_4(filename: str) -> None:
    """
    Checks if the line has exactly two parts separated by a comma.
    """
    with open(filename) as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                name, count = parts
                print(int(count) * 1000, "people named", name)
