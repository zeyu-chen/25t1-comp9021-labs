from typing import List, Generator

def f2_1() -> Generator[List[int], None, None]:
    """
    Generates rows of Pascal's triangle as an infinite sequence.
    
    Pascal's triangle is a triangular array where each number is the sum of the
    two numbers directly above it. The first row is [1], and each subsequent row
    starts and ends with 1, with each internal element being the sum of the two
    elements above it.
    
    This implementation uses list comprehension to efficiently calculate each new row
    based on the previous row.
    
    Returns:
        A generator that yields each row of Pascal's triangle as a list of integers
    
    Example:
        First few rows of Pascal's triangle:
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
        [1, 4, 6, 4, 1]
    """
    # Start with the first row of Pascal's triangle
    current_row = [1]
    yield current_row
    
    # Infinite loop to generate subsequent rows
    while True:
        # Create the next row using list comprehension:
        # - Start with 1
        # - Add pairs of adjacent elements from the current row
        # - End with 1
        current_row = [1] + [current_row[i] + current_row[i + 1] 
                            for i in range(len(current_row) - 1)] + [1]
        yield current_row


def f2_2() -> Generator[List[int], None, None]:
    """
    Generates rows of Pascal's triangle as an infinite sequence.
    
    This alternative implementation uses a more explicit approach with a loop
    to calculate each element of the new row, making the algorithm more readable
    for those unfamiliar with list comprehensions.
    
    Returns:
        A generator that yields each row of Pascal's triangle as a list of integers
    
    Example:
        First few rows of Pascal's triangle:
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
        [1, 4, 6, 4, 1]
    """
    # Start with the first row of Pascal's triangle
    current_row = [1]
    yield current_row
    
    # Infinite loop to generate subsequent rows
    while True:
        # Create a new row starting with 1
        new_row = [1]
        
        # Calculate the middle elements by adding adjacent elements from the current row
        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])
        
        # End the new row with 1
        new_row.append(1)
        
        # Update the current row and yield it
        current_row = new_row
        yield current_row
