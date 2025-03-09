def f1_1(m: int, n: int) -> str:
    """
    Creates a string pattern with m rows and n underscores per row.
    
    Uses nested list comprehensions with join method to create the pattern.
    
    Args:
        m: Number of rows
        n: Number of underscores per row
    
    Returns:
        A string with m groups of n underscores separated by '|', 
        with groups separated by ' * '
    """
    # Inner comprehension: Create n underscores joined by '|' for each row
    # Outer comprehension: Create m rows and join them with ' * '
    return ' * '.join('|'.join('_' for _ in range(n)) for _ in range(m))


def f1_2(m: int, n: int) -> str:
    """
    Creates a string pattern with m rows and n underscores per row.
    
    Uses explicit for loops with join method to create the pattern.
    
    Args:
        m: Number of rows
        n: Number of underscores per row
    
    Returns:
        A string with m groups of n underscores separated by '|',
        with groups separated by ' * '
    """
    rows = []  # Initialize list to store all rows
    for _ in range(m):  # Iterate m times to create m rows
        elements = []  # Initialize list to store elements in current row
        for _ in range(n):  # Iterate n times to create n underscores
            elements.append('_')  # Add an underscore to the current row
        row = '|'.join(elements)  # Join all underscores with '|' separator
        rows.append(row)  # Add the completed row to our collection
    return ' * '.join(rows)  # Join all rows with ' * ' separator


def f1_3(m: int, n: int) -> str:
    """
    Creates a string pattern with m rows and n underscores per row.
    
    Uses string concatenation with for loops without join method.
    
    Args:
        m: Number of rows
        n: Number of underscores per row
    
    Returns:
        A string with m groups of n underscores separated by '|',
        with groups separated by ' * '
    """
    result = ""  # Initialize empty result string
    for i in range(m):  # Iterate through each of the m rows
        for j in range(n):  # Process each of the n positions in the current row
            result += "_"  # Add an underscore at current position
            if j < n - 1:  # If not the last position in the row
                result += "|"  # Add a separator between underscores
        if i < m - 1:  # If not the last row
            result += " * "  # Add row separator
    return result


def f1_4(m: int, n: int) -> str:
    """
    Creates a string pattern with m rows and n underscores per row.
    
    Uses functional programming with map and lambda functions.
    
    Args:
        m: Number of rows
        n: Number of underscores per row
    
    Returns:
        A string with m groups of n underscores separated by '|',
        with groups separated by ' * '
    """
    # Inner map: Creates n underscores for one row
    # Outer map: Applies the inner map m times to create m rows
    # The lambda functions ignore their input (_) and just produce the required character
    # join is used to combine the results with appropriate separators
    return ' * '.join(map(lambda _: '|'.join(map(lambda _: '_', range(n))), range(m)))