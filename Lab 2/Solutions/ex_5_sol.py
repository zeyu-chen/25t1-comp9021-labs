def f5_1(L: list) -> dict:
    """
    Find elements that are between their circular neighbors in value.
    
    For each element in the list, checks if it falls between its previous
    and next neighbors in value (not index). If so, adds the element as a 
    key in the result dictionary with a tuple of (min_neighbor, max_neighbor)
    as the value.
    
    Time complexity: O(n) where n is the length of L
    Space complexity: O(k) where k is the number of elements that meet the criteria
    
    Args:
        L: A list of integers
        
    Returns:
        Dictionary mapping qualified elements to tuples of their min and max neighbors
    """
    D = {}
    for i in range(len(L)):
        m = L[i - 1]  # Previous element (wraps to last element for first position)
        n = L[(i + 1) % len(L)]  # Next element (wraps to first element for last position)
        if n < m:
            m, n = n, m  # Ensure m is the smaller value and n is the larger
        if m < L[i] < n:
            D[L[i]] = m, n  # Element is between its neighbors in value
    return D


def f5_2(L: list) -> dict:
    """
    Find elements between their circular neighbors using an extended list approach.
    
    Creates a temporary extended list by appending the first two elements to the end,
    which simplifies circular access. This avoids using modulo arithmetic
    at the cost of slightly more memory.
    
    Time complexity: O(n)
    Space complexity: O(n) due to creating the extended list
    
    Args:
        L: A list of integers
        
    Returns:
        Dictionary mapping qualified elements to tuples of their min and max neighbors
    """
    # Create extended list with wrap-around elements
    extended_L = L + L[:2]  # Add first two elements at the end
    result = {}
    
    for i in range(len(L)):
        prev_val = extended_L[i]      # Previous element
        curr_val = extended_L[i+1]    # Current element
        next_val = extended_L[i+2]    # Next element
        
        neighbors = [prev_val, next_val]
        min_neighbor = min(neighbors)
        max_neighbor = max(neighbors)
        
        if min_neighbor < curr_val < max_neighbor:
            result[curr_val] = (min_neighbor, max_neighbor)
            
    return result


def f5_3(L: list) -> dict:
    """
    Find elements between their circular neighbors using sliding window approach.
    
    Creates a 3-element window for each position in the list (considering circular
    nature) and checks if the middle element is between the min and max of its neighbors.
    This approach makes the code more readable by clearly showing the window concept.
    
    Time complexity: O(n)
    Space complexity: O(1) as we only use a fixed-size window
    
    Args:
        L: A list of integers
        
    Returns:
        Dictionary mapping qualified elements to tuples of their min and max neighbors
    """
    result = {}
    n = len(L)
    
    # For each position in the list
    for i in range(n):
        # Get three consecutive elements (with wrap-around)
        window = [L[(i-1)%n], L[i], L[(i+1)%n]]
        
        # Check if middle element is between min and max of neighbors
        if min(window[0], window[2]) < window[1] < max(window[0], window[2]):
            result[window[1]] = (min(window[0], window[2]), max(window[0], window[2]))
    
    return result