def f3_1(L: list[list[int]], half: str = 'top') -> list[list[int]]:
    """
    Swaps diagonally opposite elements in a square matrix (even side length)
    such that the element in the specified 'half' is greater than or equal 
    to its opposite.

    This implementation is based on the original provided solution.
    It uses a dictionary to define iteration ranges based on the 'half' parameter.

    Args:
        L: A square matrix (list of lists) with an even side length.
        half: Specifies which half determines the comparison/swap condition.
              Can be 'top', 'bottom', 'left', or 'right'. Defaults to 'top'.

    Returns:
        A new list representing the modified matrix. The original list L is unchanged.
    """
    # Create a deep copy of the input list L to avoid modifying it.
    # Using list comprehension for rows and list() for inner lists ensures a true copy.
    L1 = [list(row) for row in L]
    size = len(L) # Get the side length of the square matrix.
    
    # Define the iteration ranges for rows (i) and columns (j) 
    # based on the specified 'half'.
    # The ranges are designed to cover only the elements that need checking
    # according to the 'half' definition.
    ranges = {
        # For 'top', iterate through rows in the top half (0 to size/2 - 1)
        # and all columns (0 to size - 1).
        'top': (range(size // 2), range(size)),
        # For 'bottom', iterate through rows in the bottom half (size/2 to size - 1)
        # and all columns.
        'bottom': (range(size // 2, size), range(size)),
        # For 'left', iterate through all rows and columns in the left half.
        'left': (range(size), range(size // 2)),
        # For 'right', iterate through all rows and columns in the right half.
        'right': (range(size), range(size // 2, size))
    }
    
    # Get the appropriate row and column ranges for the given 'half'.
    row_range, col_range = ranges[half]
    
    # Iterate through the cells (i, j) determined by the ranges.
    for i in row_range:
        for j in col_range:
            # Calculate the indices of the diagonally opposite element.
            # Negative indices work like: L[-1] is last, L[-2] is second last.
            # So, -i-1 corresponds to (size - 1 - i).
            # Similarly, -j-1 corresponds to (size - 1 - j).
            opposite_i = -i - 1
            opposite_j = -j - 1
            
            # Compare the element L[i][j] (which is guaranteed to be in the 
            # specified 'half' by the iteration ranges) with its diagonally 
            # opposite element L[opposite_i][opposite_j].
            # Note: We compare elements from the *original* list L,
            # but perform the swap on the *copy* L1.
            if L[i][j] < L[opposite_i][opposite_j]:
                # If the element in the specified 'half' (L[i][j]) is smaller,
                # swap it with its diagonally opposite element in the copy L1.
                L1[i][j], L1[opposite_i][opposite_j] = L1[opposite_i][opposite_j], L1[i][j]
                
    # Return the modified copy of the matrix.
    return L1


def f3_2(L: list[list[int]], half: str = 'top') -> list[list[int]]:
    """
    Swaps diagonally opposite elements in a square matrix (even side length)
    such that the element in the specified 'half' is greater than or equal
    to its opposite.

    This implementation iterates through only the top half of the rows
    to process each diagonal pair exactly once. The swap condition is
    determined based on the 'half' parameter and the column index.

    Args:
        L: A square matrix (list of lists) with an even side length.
        half: Specifies which half determines the comparison/swap condition.
              Can be 'top', 'bottom', 'left', or 'right'. Defaults to 'top'.

    Returns:
        A new list representing the modified matrix. The original list L is unchanged.
    """
    size = len(L)
    # Create a deep copy to modify and return.
    L1 = [list(row) for row in L]

    # Iterate through the top half rows and all columns.
    # This ensures each diagonal pair (i, j) and (opp_i, opp_j) is considered exactly once.
    for i in range(size // 2):
        for j in range(size):
            # Calculate the indices of the diagonally opposite element.
            opp_i = size - 1 - i
            opp_j = size - 1 - j

            # Get the values from the copy L1
            val1 = L1[i][j]
            val2 = L1[opp_i][opp_j]

            # Determine if a swap is needed based on the 'half' condition.
            swap_needed = False
            if half == 'top':
                # Element (i, j) is always in the top half here.
                # It should be >= its opposite. Swap if smaller.
                if val1 < val2:
                    swap_needed = True
            elif half == 'bottom':
                # Element (opp_i, opp_j) is always in the bottom half here.
                # It should be >= its opposite. Swap if smaller.
                if val2 < val1:
                    swap_needed = True
            elif half == 'left':
                # Check which element is in the left half (j < size // 2)
                if j < size // 2: # (i, j) is in the left half
                    if val1 < val2: swap_needed = True
                else: # (opp_i, opp_j) is in the left half
                    if val2 < val1: swap_needed = True
            elif half == 'right':
                # Check which element is in the right half (j >= size // 2)
                if j >= size // 2: # (i, j) is in the right half
                    if val1 < val2: swap_needed = True
                else: # (opp_i, opp_j) is in the right half
                    if val2 < val1: swap_needed = True

            # Perform the swap on the copy L1 if needed.
            if swap_needed:
                L1[i][j], L1[opp_i][opp_j] = L1[opp_i][opp_j], L1[i][j]

    return L1
