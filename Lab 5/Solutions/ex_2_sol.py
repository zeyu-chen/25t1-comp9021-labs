def f2_1(L: list[int], n: int) -> list[int]:
    """
    Creates a list of the first n elements from an infinite sequence.
    
    The sequence is defined as:
    - Original list L
    - Followed by 2 * L (each element multiplied by 2)
    - Followed by 4 * L (each element multiplied by 4)
    - Followed by 8 * L (each element multiplied by 8)
    - And so on...
    
    This implementation uses recursion through list comprehension,
    avoiding explicit for or while loops.
    
    Args:
        L: A nonempty list of integers
        n: An integer at least equal to the length of L
        
    Returns:
        A list containing the first n elements of the sequence
    """
    # Extend L with elements from 2*L, but only if L's length is less than n
    # This recursively calls itself through the list extension mechanism
    L.extend(e * 2 for e in L if len(L) < n)
    
    # Return the first n elements of the now-extended list
    return L[:n]


def f2_2(L: list[int], n: int) -> list[int]:
    """
    Creates a list of the first n elements from an infinite sequence.
    
    The sequence is defined as:
    - Original list L
    - Followed by 2 * L (each element multiplied by 2)
    - Followed by 4 * L (each element multiplied by 4)
    - Followed by 8 * L (each element multiplied by 8)
    - And so on...
    
    This implementation uses functional programming techniques with
    power-of-2 calculation to determine which element to generate.
    
    Args:
        L: A nonempty list of integers
        n: An integer at least equal to the length of L
        
    Returns:
        A list containing the first n elements of the sequence
    """
    # Create a function to calculate any element in the infinite sequence
    def get_element_at_position(pos):
        # Find which segment the position belongs to
        # Segment 0: original list
        # Segment 1: 2 * original list
        # Segment 2: 4 * original list, etc.
        original_length = len(L)
        segment = pos // original_length
        
        # Find the index within the original list
        index = pos % original_length
        
        # Calculate multiplier: 2^segment (1 for segment 0, 2 for segment 1, etc.)
        multiplier = 1 << segment  # Efficient way to calculate 2^segment
        
        # Return the element
        return L[index] * multiplier
    
    # Generate the list using a list comprehension with our element calculation function
    return [get_element_at_position(i) for i in range(n)] 