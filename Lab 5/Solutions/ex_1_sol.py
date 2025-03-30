def f1_1(L: list[int], n: int) -> list[int]:
    """
    Extends a list by repeatedly concatenating scaled versions of itself.
    
    The function follows these steps:
    1. Keeps the original list L
    2. If n >= 1: adds 2 * L to L, resulting in L'
    3. If n >= 2: adds 3 * L' to L', resulting in L''
    4. And so on, where each iteration adds (i+1) * current_list to current_list
    
    Uses a single for loop and list comprehension for concise implementation.
    
    Args:
        L: A list of integers
        n: A non-negative integer determining the number of extensions
        
    Returns:
        The extended list after all operations
    """
    # Loop from 2 to n+1 (inclusive)
    for i in range(2, n + 2):
        # For each iteration, multiply each element of L by i and extend L
        # This effectively appends i * L to L
        L.extend([e * i for e in L])
    return L


def f1_2(L: list[int], n: int) -> list[int]:
    """
    Extends a list by repeatedly concatenating scaled versions of itself.
    
    This implementation uses a simpler approach with more explicit steps:
    1. For each step from 1 to n, we calculate the current multiplier
    2. Create a new portion by multiplying each element in the current list
    3. Extend the list with this new portion
    
    Args:
        L: A list of integers
        n: A non-negative integer determining the number of extensions
        
    Returns:
        The extended list after all operations
    """
    # Make a copy of the original list to avoid modifying the input directly
    # (though the problem doesn't require this, it's a good practice)
    result = L.copy()
    
    # Process each step from 1 to n
    for step in range(1, n + 1):
        # The multiplier for this step is step + 1 (2, 3, 4, ...)
        multiplier = step + 1
        
        # Get the current length of the list before we add new elements
        current_length = len(result)
        
        # Create the new portion by multiplying each element in the current list
        new_portion = []
        for i in range(current_length):
            new_portion.append(result[i] * multiplier)
        
        # Add the new portion to the result
        result.extend(new_portion)
    
    return result