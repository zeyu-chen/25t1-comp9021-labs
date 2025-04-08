# Assume that the argument L is a list of integers.
#
# Lists are, if possible, broken down into sublists
# all the same length, that length being maximal,
# those sublists themselves being, if possible,
# broken down into sublists all the same length,
# that length being maximal...
#
# The original list is preserved.

from math import sqrt
from typing import List, Any, Union

def f4_1(L: List[int]) -> Union[List[Any], List[int]]:
    """
    Recursively breaks down a list into nested sublists of maximal equal length.

    This implementation searches for the largest divisor of the list length
    that is less than or equal to the square root of the length. If found,
    it divides the list into sublists of that length and recursively applies
    the same process to each sublist.

    Args:
        L: A list of integers

    Returns:
        A new list that may contain nested sublists, or a copy of the original list
        if no further breakdown is possible

    Example:
        f4_1([1, 2, 3, 4]) returns [[1, 2], [3, 4]]
        f4_1([1, 2, 3, 4, 5, 6]) returns [[1, 2, 3], [4, 5, 6]]
        f4_1([1, 2, 3, 4, 5, 6, 7, 8, 9]) returns [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    # Handle empty list or single element list
    if len(L) <= 1:
        return list(L)

    # Search for the largest divisor <= sqrt(len(L))
    for n in range(2, round(sqrt(len(L))) + 1):
        if len(L) % n == 0:
            # Calculate the width of each sublist
            w = len(L) // n
            # Create n sublists of width w and recursively process each
            return [f4_1(L[i : i + w]) for i in range(0, len(L), w)]

    # If no suitable divisor is found, return a copy of the list
    return list(L)


def f4_2(L: List[int]) -> Union[List[Any], List[int]]:
    """
    Recursively breaks down a list into nested sublists of maximal equal length.

    This alternative implementation uses a different approach that focuses on
    creating a balanced binary-like tree structure. It first tries to split the list
    into two equal parts, then recursively processes each part.

    Args:
        L: A list of integers

    Returns:
        A new list that may contain nested sublists, or a copy of the original list
        if no further breakdown is possible

    Example:
        f4_2([1, 2, 3, 4]) returns [[1, 2], [3, 4]]
        f4_2([1, 2, 3, 4, 5, 6]) returns [[1, 2, 3], [4, 5, 6]]
        f4_2([1, 2, 3, 4, 5, 6, 7, 8, 9]) returns [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    # Handle empty list or single element list
    if len(L) <= 1:
        return list(L)

    # Try to find divisors of the list length
    length = len(L)
    divisors = []

    # Find all divisors
    for i in range(2, int(sqrt(length)) + 1):
        if length % i == 0:
            divisors.append(i)
            if i != length // i:
                divisors.append(length // i)

    # If no divisors found, return a copy of the list
    if not divisors:
        return list(L)

    # Sort divisors
    divisors.sort()

    # For other cases, use the smallest divisor
    smallest_divisor = divisors[0]
    chunk_size = length // smallest_divisor

    # Create chunks and recursively process each
    result = []
    for i in range(0, length, chunk_size):
        chunk = L[i:i + chunk_size]
        result.append(f4_2(chunk))

    return result

