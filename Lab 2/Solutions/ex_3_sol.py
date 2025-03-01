def f3_1(L: list) -> list:
    """
    Remove matching elements from both ends of the list until they no longer match.
    
    This implementation uses list.pop() operations which are O(n) for pop(0),
    making the overall time complexity O(n²) in worst case.
    
    Args:
        L (list): The input list to process
        
    Returns:
        list: The modified list with matching end elements removed
    """
    while len(L) > 1 and L[0] == L[-1]:
        L.pop(0)  # O(n) operation - must shift all elements
        L.pop()   # O(1) operation - removes from the end
    return L


def f3_2(L: list) -> list:
    """
    Remove matching elements from both ends of the list using deque.
    
    Uses collections.deque which provides O(1) operations at both ends,
    improving time complexity to O(n) compared to list.pop(0).
    This approach is more efficient but creates a new data structure.
    
    Args:
        L (list): The input list to process
        
    Returns:
        list: A new list with matching end elements removed
    """
    from collections import deque
    # Convert to deque for efficient operations at both ends
    d = deque(L)
    while len(d) > 1 and d[0] == d[-1]:
        d.popleft()  # O(1) operation
        d.pop()      # O(1) operation
    return list(d)


def f3_3(L: list) -> list:
    """
    Remove matching elements from both ends using slice operation.
    
    This approach calculates how many pairs match from both ends,
    then returns the appropriate slice in a single operation.
    Most efficient solution with O(n) time complexity and no 
    intermediate data structures.
    
    Args:
        L (list): The input list to process
        
    Returns:
        list: A new list with matching end elements removed
    """
    # Find how many matching pairs from both ends
    i = 0
    while i < len(L) // 2 and L[i] == L[-i-1]:
        i += 1
    # Return the middle portion of the list
    return L[i:len(L)-i]