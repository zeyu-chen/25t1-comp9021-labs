def f4(D: dict[int, int], n: int) -> list[int]:
    if n not in D:
        return []
    
    L = [n]
    while n in D and n < D[n]:
        n = D[n]
        L.append(n)

    return L