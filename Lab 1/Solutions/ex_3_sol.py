def f3(L: list[int]) -> None:
    while len(L) > 1 and L[-2] < L[-1]:
        L.remove(L[-2])
    print(L)