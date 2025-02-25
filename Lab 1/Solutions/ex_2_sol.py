def f2_1(n: int) -> str:
    """
    Creates a pattern where each of the n lines contains n repetitions of the digit n.
    Uses nested string multiplication for concise implementation.
    """
    if n == 0:
        return ""
    return (str(n) * n + "\n") * n


def f2_2(n: int) -> str:
    """
    Creates a pattern where each of the n lines contains n repetitions of the digit n.
    Implements the solution using a for loop to build rows.
    """
    if n == 0:
        return ""
    
    result = ""
    for _ in range(n):
        result += str(n) * n + "\n"
    return result


def f2_3(n: int) -> str:
    """
    Creates a pattern where each of the n lines contains n repetitions of the digit n.
    Uses list comprehension and join for elegant construction.
    """
    if n == 0:
        return ""
    
    rows = [str(n) * n for _ in range(n)]
    return "\n".join(rows) + "\n"


def f2_4(n: int) -> str:
    """
    Creates a pattern where each of the n lines contains n repetitions of the digit n.
    Uses nested loops for explicit row and column construction.
    """
    if n == 0:
        return ""
    
    result = ""
    for _ in range(n):
        row = ""
        for _ in range(n):
            row += str(n)
        result += row + "\n"
    return result


def f2_5(n: int) -> str:
    """
    Creates a pattern where each of the n lines contains n repetitions of the digit n.
    Uses string formatting with repetition.
    """
    if n == 0:
        return ""
    
    line = "{}".format(str(n) * n)
    return "\n".join([line] * n) + "\n"


