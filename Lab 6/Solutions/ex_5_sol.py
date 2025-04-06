def f5_1(L: list[list[int]]) -> None:
    """
    Computes row and column sums for each element in a 2D list L,
    and prints a grid of colored squares based on the sign of the total sum
    (row sum + column sum - element itself).

    This implementation uses NumPy for array conversion and summation,
    then iterates through the array to calculate and print the result.

    Args:
        L: A list of lists of integers (potentially empty or non-rectangular).
    """
    import numpy as np

    # Handle empty input list
    if not L or not L[0]:
        print("") # Or handle as appropriate, e.g., print nothing
        return

    # Convert the input list to a NumPy array for easier calculations.
    L_array = np.array(L)
    rows, cols = L_array.shape

    # Pre-calculate sums for all rows and columns.
    # axis=1 sums across columns (for each row). Result shape: (rows,)
    row_sums = np.sum(L_array, axis=1)
    # axis=0 sums across rows (for each column). Result shape: (cols,)
    col_sums = np.sum(L_array, axis=0)

    # Define the mapping from sign (-1, 0, 1) to color squares.
    color_map = {0: '🟦', 1: '🟩', -1: '🟥'}

    # Iterate through each element of the original array structure.
    for i in range(rows):
        output_row = [] # Store the colors for the current row
        for j in range(cols):
            # Calculate the total sum for cell (i, j).
            # Sum of row i + sum of column j - value at (i, j) itself
            # (as per original solution logic, the element itself is subtracted).
            # Note: The problem description asks for sum of row + sum of column,
            # but the provided solution subtracts the element. We follow the solution.
            total_sum = row_sums[i] + col_sums[j] - L_array[i, j]
            
            # Determine the sign of the total sum.
            sign = np.sign(total_sum)
            
            # Get the corresponding color from the map.
            color = color_map[sign]
            output_row.append(color)
            
        # Print the row of colors.
        print(*output_row, sep='')

def f5_2(L: list[list[int]]) -> None:
    """
    Computes row and column sums for each element in a 2D list L,
    and prints a grid of colored squares based on the sign of the total sum
    (row sum + column sum - element itself), using NumPy broadcasting.

    This implementation leverages NumPy broadcasting to calculate all total sums
    simultaneously, minimizing explicit Python loops.

    Args:
        L: A list of lists of integers (potentially empty or non-rectangular).
    """
    import numpy as np

    # Handle empty input list
    if not L or not L[0]:
        print("")
        return

    # Convert to NumPy array.
    L_array = np.array(L)
    rows, cols = L_array.shape

    # Calculate row sums and reshape to a column vector (rows, 1).
    # Keepdims=True maintains the dimension, resulting in shape (rows, 1).
    row_sums = np.sum(L_array, axis=1, keepdims=True)
    
    # Calculate column sums and reshape to a row vector (1, cols).
    # Keepdims=True maintains the dimension, resulting in shape (1, cols).
    col_sums = np.sum(L_array, axis=0, keepdims=True)

    # Use broadcasting to add row sums and column sums.
    # row_sums (rows, 1) + col_sums (1, cols) -> results in a (rows, cols) array
    # where result[i, j] = row_sums[i] + col_sums[j].
    # Then subtract the original array element-wise.
    total_sums_matrix = row_sums + col_sums - L_array

    # Calculate the sign for each element in the total sums matrix.
    signs_matrix = np.sign(total_sums_matrix)

    # Create the output grid using boolean indexing based on signs.
    # Initialize with the character for sign 0 ('🟦').
    output_grid = np.full(L_array.shape, '🟦', dtype='U1')
    # Where sign is 1, set to '🟩'.
    output_grid[signs_matrix == 1] = '🟩'
    # Where sign is -1, set to '🟥'.
    output_grid[signs_matrix == -1] = '🟥'

    # Print the resulting grid of colors.
    for row in output_grid:
        print(*row, sep='')
