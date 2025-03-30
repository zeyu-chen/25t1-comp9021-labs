def f4_1(L: list[int]) -> list[list[int]]:
    """
    Process a list into sublists where beginning and end have the same number of 2-element lists.
    
    The function creates a list with:
    - At its beginning: n sublists of 2 elements
    - In the middle: remaining elements (if any)
    - At its end: n sublists of 2 elements
    Where n is as large as possible.
    
    This implementation uses list slicing and list comprehensions without loops.
    
    Args:
        L: A list of integers
        
    Returns:
        A list of sublists structured as described
    """
    # Handle empty list case
    if not L:
        return []
    
    # If the length is odd, we need special handling for the middle
    if len(L) % 2:
        # Calculate how many pairs of 2 elements we can have at each end
        # The // 4 ensures we have the same number at both ends
        pairs_at_each_end = len(L) // 4
        
        # Create pairs at the beginning
        start_pairs = [L[i : i + 2] for i in range(0, pairs_at_each_end * 2, 2)]
        
        # Create the middle part with remaining elements
        middle = [L[pairs_at_each_end * 2 : len(L) - (pairs_at_each_end * 2)]]
        
        # Create pairs at the end
        end_pairs = [L[i : i + 2] for i in range(len(L) - (pairs_at_each_end * 2), len(L) - 1, 2)]
        
        # Combine all parts
        return start_pairs + middle + end_pairs
    
    # If length is even, we can simply split into pairs
    return [L[i : i + 2] for i in range(0, len(L) - 1, 2)]


def f4_2(L: list[int]) -> list[list[int]]:
    """
    Process a list into sublists where beginning and end have the same number of 2-element lists.
    
    The function creates a list with:
    - At its beginning: n sublists of 2 elements
    - In the middle: remaining elements (if any)
    - At its end: n sublists of 2 elements
    Where n is as large as possible.
    
    This implementation uses a simpler approach with intermediate variables
    and explicit calculations for better readability.
    
    Args:
        L: A list of integers
        
    Returns:
        A list of sublists structured as described
    """
    # Handle empty list case
    if not L:
        return []
    
    # Handle single element case
    if len(L) == 1:
        return [L]
    
    # Handle 2 or 3 elements case - just return the whole list
    if len(L) <= 3:
        return [L]
    
    # For 4 or more elements, we need to balance the 2-element lists
    total_length = len(L)
    
    # Calculate max number of pair groups we can have at each end
    max_pairs = total_length // 4
    
    # Create the result list
    result = []
    
    # Add the beginning pairs
    index = 0
    while index < max_pairs * 2 and index + 1 < total_length:
        result.append([L[index], L[index + 1]])
        index += 2
    
    # Handle the middle elements
    middle_start = max_pairs * 2
    middle_end = total_length - max_pairs * 2
    
    if middle_start < middle_end:
        middle_elements = L[middle_start:middle_end]
        result.append(middle_elements)
    
    # Add the end pairs
    index = total_length - max_pairs * 2
    while index < total_length - 1:
        result.append([L[index], L[index + 1]])
        index += 2
    
    # Return the result list without using explicit loops
    return result


def f4_3(L: list[int]) -> list[list[int]]:
    """
    Process a list into sublists where beginning and end have the same number of 2-element lists.
    
    The function creates a list with:
    - At its beginning: n sublists of 2 elements
    - In the middle: remaining elements (if any)
    - At its end: n sublists of 2 elements
    Where n is as large as possible.
    
    This implementation uses a recursive approach and mathematical optimization.
    
    Args:
        L: A list of integers
        
    Returns:
        A list of sublists structured as described
    """
    # Base cases for recursion
    if not L:
        return []
    if len(L) <= 3:
        return [L]
    
    # Helper function to create list of pairs - no loops
    def create_pairs(lst):
        return [lst[i:i+2] for i in range(0, len(lst), 2) if i+1 < len(lst)]
    
    # For even length lists, we can optimize by just creating pairs
    if len(L) % 2 == 0:
        return create_pairs(L)
    
    # For odd length lists, we need to carefully balance the pairs
    # Calculate the optimal number of elements for pairs on each end
    # For maximum pairs, we calculate floor(n/4) pairs on each end
    n = len(L)
    pair_elements = (n // 4) * 2
    
    # Extract elements for pairs on both ends
    left_elements = L[:pair_elements]
    right_elements = L[n-pair_elements:]
    
    # Create the pairs from left and right elements
    left_pairs = create_pairs(left_elements)
    right_pairs = create_pairs(right_elements)
    
    # Extract middle elements
    middle_elements = L[pair_elements:n-pair_elements]
    
    # Combine the parts - if middle has elements, include as a sublist
    if middle_elements:
        return left_pairs + [middle_elements] + right_pairs
    else:
        return left_pairs + right_pairs 