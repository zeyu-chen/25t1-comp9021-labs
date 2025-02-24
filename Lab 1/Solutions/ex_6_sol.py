def f6(filename: str) -> None:
    with open(filename) as file:
        for line in file:
            if not line.strip():
                continue
            count, symbol = line.split()
            if count:
                print(int(count) * symbol)