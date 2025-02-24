def f5(filename: str) -> None:
    with open(filename) as file:
        for line in file:
            name, count = line.split(",")
            print(int(count) * 1000, "people named", name)