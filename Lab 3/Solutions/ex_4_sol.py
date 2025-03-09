def f4_1(n: int, base: int) -> dict[int, tuple[int]]:
    """
    Creates a dictionary mapping integers from 0 to n to their representation in the specified base.
    
    Uses iterative division by base to convert decimal numbers to the target base.
    
    Args:
        n: The upper limit of numbers to convert (inclusive)
        base: The target base (between 2 and 9)
    
    Returns:
        A dictionary where keys are integers from 0 to n and values are tuples 
        representing those numbers in the specified base
    """
    # Initialize dictionary with special case for 0
    D = {0: (0,)}
    
    # Process each number from 1 to n
    for m in range(1, n + 1):
        digits = []  # List to store digits in reverse order
        p = m  # Working copy of the number
        
        # Convert decimal to the specified base
        while p:
            digits.append(p % base)  # Get remainder (current digit)
            p //= base  # Integer division to get quotient
            
        # Reverse digits to get correct order and convert to tuple
        D[m] = tuple(reversed(digits))
        
    return D


def f4_2(n: int, base: int) -> dict[int, tuple[int]]:
    """
    Creates a dictionary mapping integers from 0 to n to their representation in the specified base.
    
    Uses recursion to convert decimal numbers to the target base.
    
    Args:
        n: The upper limit of numbers to convert (inclusive)
        base: The target base (between 2 and 9)
    
    Returns:
        A dictionary where keys are integers from 0 to n and values are tuples 
        representing those numbers in the specified base
    """
    # Recursive function to convert a number to a specified base
    def to_base(num):
        # Base case
        if num == 0:
            return (0,)
        
        # Recursive case
        if num < base:
            return (num,)  # Single digit case
        else:
            # Get the representation of the quotient, then append the remainder
            return to_base(num // base) + (num % base,)
    
    # Build dictionary using dictionary comprehension
    result = {m: to_base(m) if m > 0 else (0,) for m in range(n + 1)}
    return result


def f4_3(n: int, base: int) -> dict[int, tuple[int]]:
    """
    Creates a dictionary mapping integers from 0 to n to their representation in the specified base.
    
    Uses Python's divmod function for cleaner code and more efficient conversion.
    
    Args:
        n: The upper limit of numbers to convert (inclusive)
        base: The target base (between 2 and 9)
    
    Returns:
        A dictionary where keys are integers from 0 to n and values are tuples 
        representing those numbers in the specified base
    """
    result = {}
    
    # Handle special case for 0
    result[0] = (0,)
    
    # Process each number from 1 to n
    for num in range(1, n + 1):
        digits = []
        temp = num
        
        # Convert using divmod for cleaner code
        while temp > 0:
            # divmod returns quotient and remainder in one operation
            temp, remainder = divmod(temp, base)
            digits.append(remainder)
            
        # Reverse digits and convert to tuple
        result[num] = tuple(reversed(digits))
        
    return result


def f4_4(n: int, base: int) -> dict[int, tuple[int]]:
    """
    Creates a dictionary mapping integers from 0 to n to their representation in the specified base.
    
    Uses list comprehensions for more concise, functional-style code.
    
    Args:
        n: The upper limit of numbers to convert (inclusive)
        base: The target base (between 2 and 9)
    
    Returns:
        A dictionary where keys are integers from 0 to n and values are tuples 
        representing those numbers in the specified base
    """
    # Helper function to convert a single number to the specified base
    def convert_to_base(num):
        # Special case for 0
        if num == 0:
            return (0,)
            
        # Generate digits in reverse order
        digits_reversed = []
        temp = num
        
        while temp > 0:
            digits_reversed.append(temp % base)
            temp //= base
            
        # Return tuple of digits in correct order
        return tuple(reversed(digits_reversed))
    
    # Build dictionary using dictionary comprehension and the helper function
    return {m: convert_to_base(m) for m in range(n + 1)}
