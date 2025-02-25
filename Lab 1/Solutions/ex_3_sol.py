def f3_1(L: list[int]) -> None:
    """
    Removes elements from L using a while loop and remove method.
    Checks from right to left, removing elements smaller than their successors.
    """
    while len(L) > 1 and L[-2] < L[-1]:
        L.remove(L[-2])
    print(L)