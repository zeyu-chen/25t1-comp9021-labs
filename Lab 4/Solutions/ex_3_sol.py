def f3_1(L: list) -> list:
    """
    Removes elements from a list where the element is the arithmetic mean of its neighbors.
    
    Iterates through the list and removes any element that is equal to the average
    of its immediate neighbors (i.e., where L[i] = (L[i-1] + L[i+1])/2).
    Continues this process until no more elements can be removed.
    
    Args:
        L: A list of numbers
        
    Returns:
        The modified list with arithmetic mean elements removed
    """
    # Initialize index
    i = 0
    
    # Iterate through the list with walrus operator to increment i
    while (i := i + 1) < len(L) - 1:
        # Check if current element is arithmetic mean of neighbors
        if L[i - 1] + L[i + 1] == L[i] * 2:
            # Remove the current element
            L.pop(i)
            # Decrement index since we removed an element
            i -= 1
            
    # Return the modified list
    return L


def f3_2(L: list) -> list:
    """
    Removes elements from a list where the element is the arithmetic mean of its neighbors.
    
    Uses a loop that continues until the list stabilizes, with a backward iteration
    approach in each pass to avoid index issues when removing elements.
    
    Args:
        L: A list of numbers
        
    Returns:
        The modified list with arithmetic mean elements removed
    """
    # Create a copy to avoid modifying the input list directly
    result = L.copy()
    
    # Continue until no more elements can be removed
    changed = True
    while changed and len(result) > 2:
        changed = False
        
        # Iterate through the list backwards to avoid index shifting problems
        i = len(result) - 2
        while i > 0:
            # Check if current element is arithmetic mean of neighbors
            if result[i - 1] + result[i + 1] == result[i] * 2:
                # Remove the current element
                result.pop(i)
                changed = True
            i -= 1
    
    # Return the modified list
    return result


def f3_3(L: list) -> list:
    """
    Removes elements from a list where the element is the arithmetic mean of its neighbors.
    
    Uses recursive filtering approach, repeatedly building new lists until no more 
    elements can be removed.
    
    Args:
        L: A list of numbers
        
    Returns:
        A new list with arithmetic mean elements removed
    """
    # Handle edge cases
    if len(L) <= 2:
        return L.copy()
    
    # Function to check if any element is the arithmetic mean of its neighbors
    def has_arithmetic_mean(lst):
        for i in range(1, len(lst) - 1):
            if lst[i - 1] + lst[i + 1] == lst[i] * 2:
                return True
        return False
    
    # Function to filter out elements that are arithmetic means of their neighbors
    def filter_one_pass(lst):
        if len(lst) <= 2:
            return lst.copy()
            
        result = [lst[0]]  # First element is always kept
        
        # Filter middle elements
        for i in range(1, len(lst) - 1):
            if lst[i - 1] + lst[i + 1] != lst[i] * 2:
                result.append(lst[i])
                
        result.append(lst[-1])  # Last element is always kept
        return result
    
    # Apply filtering passes until the list stabilizes
    current = L.copy()
    while has_arithmetic_mean(current):
        current = filter_one_pass(current)
        
    return current