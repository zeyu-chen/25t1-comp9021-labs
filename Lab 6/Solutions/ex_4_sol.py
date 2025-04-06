def f4_1(n: int, black_centre: bool = True) -> None:
    """
    Prints an n x n checkerboard pattern using NumPy arrays and layer filling.

    This implementation builds the pattern from the outside in, filling 
    concentric square layers with alternating colors.

    Args:
        n: The side length of the checkerboard (n >= 1).
        black_centre: If True, the center of the board tends towards black.
                      If False, the center tends towards white.
                      The exact color depends on n's parity and the pattern.
    """
    import numpy as np

    def black(i: int, black_centre: bool) -> bool:
        """
        Helper function (defined inside f4_1) to determine if a layer/ring should start with black.
        Determines the color based on layer size `i` and the `black_centre` flag.
        The logic `i % 4 in {1, 2}` creates a pattern like B, B, W, W, B...
        The XOR `^ (not black_centre)` flips this pattern if the center should be white.
        """
        return (i % 4 in {1, 2}) ^ (not black_centre)

    # Determine the color of the outermost square (n x n).
    initial_color = '⬛' if black(n, black_centre) else '⬜'
    
    # Create the initial n x n grid filled with the determined outermost color.
    grid = np.full((n, n), initial_color)
    
    # Fill inner layers iteratively.
    for i in range(1, n // 2 + 1):
        # Determine the color for the current inner layer (size n - 2*i).
        layer_color = '⬛' if black(n - 2 * i, black_centre) else '⬜'
        # Assign the color to the inner square slice.
        grid[i : n - i, i : n - i] = layer_color
        
    # Print the final grid row by row.
    for row in grid:
        print(*row, sep='')



