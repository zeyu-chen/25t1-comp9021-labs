def f1_1(m: int, n: int) -> str:
    """
    Creates a pattern of m segments, each containing a pair of vertical bars with n underscores between them.
    Uses string multiplication for direct concatenation.
    """
    return ("|" + "_" * n + "|") * m


def f1_2(m: int, n: int) -> str:
    """
    Creates a pattern of m segments, each containing a pair of vertical bars with n underscores between them.
    Implements the solution using a for loop and string concatenation.
    """
    result = ""
    for _ in range(m):
        result += "|" + "_" * n + "|"
    return result


def f1_3(m: int, n: int) -> str:
    """
    Creates a pattern of m segments, each containing a pair of vertical bars with n underscores between them.
    Implements the solution using a while loop with a counter variable.
    """
    result = ""
    i = 0
    while i < m:
        result += "|" + "_" * n + "|"
        i += 1
    return result


def f1_4(m: int, n: int) -> str:
    """
    Creates a pattern of m segments, each containing a pair of vertical bars with n underscores between them.
    Implements the solution using recursion with base cases for m=0 and m=1.
    """
    if m == 0:
        return ""
    if m == 1:
        return "|" + "_" * n + "|"
    return "|" + "_" * n + "|" + f1_4(m - 1, n)
