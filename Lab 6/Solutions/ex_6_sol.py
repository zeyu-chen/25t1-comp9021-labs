# Lab 6 Exercise 6 Solutions

def f6_1(L: list[list[int]]) -> None:
    """
    Computes row+column sums for each element in a square matrix L,
    and prints a grid of colored squares based on the sign of the total sum
    (row sum + column sum - element itself).

    This implementation is based on the original provided solution.
    It uses NumPy broadcasting and np.vectorize to achieve the result
    with no explicit Python loops for computation.

    Args:
        L: A non-empty square matrix (list of lists of integers).
           Assumes input is valid as per problem description.
    """
    import numpy as np

    # Convert the input list to a NumPy array.
    L_array = np.array(L)

    # Calculate row sums and reshape to a column vector (N, 1) using np.newaxis.
    row_sums = np.sum(L_array, axis=1)[:, np.newaxis]
    # Equivalent using keepdims=True: row_sums = np.sum(L_array, axis=1, keepdims=True)

    # Calculate column sums. Summing the transpose L_array.T along axis=1 gives column sums
    # of the original array. Result is a row vector (1, N) implicitly, or (N,) if keepdims=False.
    # The original solution uses L1.T and sums axis=1, result shape (N,)
    # which broadcasts correctly with (N, 1) row_sums.
    col_sums = np.sum(L_array.T, axis=1)
    # Alternative using axis=0 on original: col_sums = np.sum(L_array, axis=0) # Shape (N,)
    # Alternative keeping dims: col_sums = np.sum(L_array, axis=0, keepdims=True) # Shape (1, N)

    # Calculate the total sum for each cell using broadcasting.
    # row_sums (N, 1) + col_sums (N,) broadcasts to (N, N).
    # Subtract the original element values.
    # This follows the original solution's formula, potentially differing from the text description.
    total_sums_matrix = row_sums + col_sums - L_array

    # Calculate the sign (-1, 0, or 1) for each element in the total sums matrix.
    signs_matrix = np.sign(total_sums_matrix)

    # Define a mapping function (lambda) to convert sign to color.
    sign_to_color = lambda sign_value: {0: '🟦', 1: '🟩', -1: '🟥'}[sign_value]

    # Use np.vectorize to apply the mapping function element-wise to the signs_matrix.
    # This creates a new NumPy array of the same shape, containing color strings.
    vectorized_mapper = np.vectorize(sign_to_color)
    color_grid = vectorized_mapper(signs_matrix)

    # Print the resulting grid of colors, row by row.
    # This is the only allowed loop as per the problem statement.
    for row in color_grid:
        print(*row, sep='')

def f6_2(L: list[list[int]]) -> None:
    """
    Computes row+column sums for each element in a square matrix L,
    and prints a grid of colored squares based on the sign of the total sum
    (row sum + column sum - element itself).

    This implementation uses NumPy broadcasting and boolean indexing
    to create the color grid, avoiding np.vectorize.

    Args:
        L: A non-empty square matrix (list of lists of integers).
           Assumes input is valid as per problem description.
    """
    import numpy as np

    # Convert the input list to a NumPy array.
    L_array = np.array(L)
    rows, cols = L_array.shape # Assuming square, rows == cols

    # Calculate row sums, keeping dimension for broadcasting (rows, 1).
    row_sums = np.sum(L_array, axis=1, keepdims=True)

    # Calculate column sums, keeping dimension for broadcasting (1, cols).
    col_sums = np.sum(L_array, axis=0, keepdims=True)

    # Calculate the total sum for each cell using broadcasting.
    # Subtracting the original element as per the original solution's logic.
    total_sums_matrix = row_sums + col_sums - L_array

    # Calculate the sign (-1, 0, or 1) for each element.
    signs_matrix = np.sign(total_sums_matrix)

    # Create the output grid using boolean indexing based on signs.
    # Initialize with the character for sign 0 ('🟦').
    # Using dtype='U1' for single Unicode character storage.
    output_grid = np.full(L_array.shape, '🟦', dtype='U1')

    # Where sign is 1 (positive sum), set the element to '🟩'.
    output_grid[signs_matrix == 1] = '🟩'

    # Where sign is -1 (negative sum), set the element to '🟥'.
    output_grid[signs_matrix == -1] = '🟥'

    # Print the resulting grid of colors.
    # This loop is for printing only.
    for row in output_grid:
        print(*row, sep='') 