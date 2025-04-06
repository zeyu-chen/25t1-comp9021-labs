# Lab 6 Exercise 2 Solutions

def f2_1(L: list[list[int]], i: int, j: int, major: bool = True) -> int:
    """
    Calculates the sum of elements on a specified diagonal of a square matrix
    that passes through the element at (i, j).

    This is the direct adaptation of the original provided solution,
    using the walrus operator (:=) for concise index updates during traversal.

    Args:
        L: A square matrix represented as a list of lists of integers.
        i: The 1-based row index of the element the diagonal passes through.
        j: The 1-based column index of the element the diagonal passes through.
        major: If True (default), calculate the sum of the major diagonal (NW-SE).
               If False, calculate the sum of the minor diagonal (SW-NE).

    Returns:
        The sum of the elements on the specified diagonal passing through (i, j).
    """
    # Convert 1-based indices to 0-based. Note: 'i' and 'j' are reassigned here.
    i1 = i = i - 1 
    j1 = j = j - 1
    # Start sum with the central element.
    the_sum = L[i1][j1]
    
    if major:
        # Major Diagonal (NW-SE)
        # Traverse NW (up-left). The walrus operator (:=) updates i1 and j1 *within* the condition check.
        while (i1 := i1 - 1) >= 0 and (j1 := j1 - 1) >= 0:
            the_sum += L[i1][j1]
        # Reset indices to the starting 0-based point for the second traversal direction.
        i1, j1 = i, j 
        # Traverse SE (down-right).
        while (i1 := i1 + 1) < len(L) and (j1 := j1 + 1) < len(L):
            the_sum += L[i1][j1]
    else:
        # Minor Diagonal (SW-NE)
        # Traverse NE (up-right).
        while (i1 := i1 - 1) >= 0 and (j1 := j1 + 1) < len(L):
            the_sum += L[i1][j1]
        # Reset indices.
        i1, j1 = i, j 
        # Traverse SW (down-left).
        while (i1 := i1 + 1) < len(L) and (j1 := j1 - 1) >= 0:
            the_sum += L[i1][j1]
            
    return the_sum


def f2_2(L: list[list[int]], i: int, j: int, major: bool = True) -> int:
    """
    Calculates the sum of elements on a specified diagonal of a square matrix
    that passes through the element at (i, j).

    This version iterates through all elements of the matrix and checks 
    if each element belongs to the specified diagonal using mathematical conditions.

    Args:
        L: A square matrix represented as a list of lists of integers.
        i: The 1-based row index of the element the diagonal passes through.
        j: The 1-based column index of the element the diagonal passes through.
        major: If True (default), calculate the sum of the major diagonal (NW-SE).
               If False, calculate the sum of the minor diagonal (SW-NE).

    Returns:
        The sum of the elements on the specified diagonal passing through (i, j).
    """
    size = len(L)  # Get the size of the square matrix.
    the_sum = 0   # Initialize the sum.

    # Convert 1-based input indices (i, j) to 0-based for calculations.
    target_row_0based = i - 1
    target_col_0based = j - 1

    # Calculate the diagonal constants based on the target point (i, j).
    if major:
        # For the major diagonal, the difference (row - col) is constant.
        diagonal_constant = target_row_0based - target_col_0based
    else:
        # For the minor diagonal, the sum (row + col) is constant.
        diagonal_constant = target_row_0based + target_col_0based

    # Iterate through each cell (row, col) of the matrix using 0-based indices.
    for row in range(size):
        for col in range(size):
            if major:
                # Check if the current cell lies on the target major diagonal.
                if row - col == diagonal_constant:
                    the_sum += L[row][col]
            else:
                # Check if the current cell lies on the target minor diagonal.
                if row + col == diagonal_constant:
                    the_sum += L[row][col]
                    
    return the_sum 


def f2_3(L: list[list[int]], i: int, j: int, major: bool = True) -> int:
    """
    Calculates the sum of elements on a specified diagonal using list comprehension.

    This version iterates through all indices and sums elements satisfying
    the diagonal condition, expressed concisely using sum() and a generator expression.

    Args:
        L: A square matrix represented as a list of lists of integers.
        i: The 1-based row index of the element the diagonal passes through.
        j: The 1-based column index of the element the diagonal passes through.
        major: If True (default), calculate the sum of the major diagonal (NW-SE).
               If False, calculate the sum of the minor diagonal (SW-NE).

    Returns:
        The sum of the elements on the specified diagonal passing through (i, j).
    """
    size = len(L)
    # Convert 1-based target indices to 0-based
    target_row_0 = i - 1
    target_col_0 = j - 1

    if major:
        # Major diagonal condition: row - col == constant
        # Calculate the constant based on the target point (i, j)
        constant = target_row_0 - target_col_0
        # Use a generator expression within sum() to iterate and filter
        return sum(L[r][c] for r in range(size) for c in range(size) if r - c == constant)
    else:
        # Minor diagonal condition: row + col == constant
        # Calculate the constant based on the target point (i, j)
        constant = target_row_0 + target_col_0
        # Use a generator expression within sum() to iterate and filter
        return sum(L[r][c] for r in range(size) for c in range(size) if r + c == constant) 