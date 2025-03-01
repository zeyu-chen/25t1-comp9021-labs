def f4_1(L: list) -> list:
    """
    Remove elements equal to their indices from a list using iteration.
    
    This is the direct implementation of the problem statement.
    When an element is removed, all subsequent elements shift left,
    changing their indices, which is why we don't increment i after removal.
    
    Time complexity: O(n²) due to L.pop(i) being O(n)
    Space complexity: O(1) as we modify the list in-place
    
    Args:
        L: A list of integers (assumed to be in increasing order)
        
    Returns:
        The modified list with elements equal to their indices removed
    """
    i = 0
    while i < len(L):
        if L[i] == i:
            L.pop(i)  # Remove the element at index i
            # Don't increment i since all elements shifted left
        else:
            i += 1  # Element doesn't match its index, move to next
    return L


def f4_2(L: list) -> list:
    """
    Remove elements equal to their indices using a single-pass approach.
    
    This implementation builds a new list by tracking the current index
    after each decision to include/exclude an element. This avoids the
    O(n) cost of pop operations.
    
    Time complexity: O(n)
    Space complexity: O(n) for the result list
    
    Args:
        L: A list of integers (assumed to be in increasing order)
        
    Returns:
        A new list with elements equal to their indices removed
    """
    ans = []
    curr_idx = 0
    
    for val in L:
        if val != curr_idx:
            # Only keep values that don't match their effective index
            ans.append(val)
            curr_idx += 1
            
    return ans


def f4_3(L: list) -> list:
    """
    Remove elements equal to their indices using recursion.
    
    This recursive approach handles the index shifting by updating
    the index only when keeping an element. It creates new list objects
    during recursion to avoid modifying the original list.
    
    Time complexity: O(n²) due to slicing operations
    Space complexity: O(n) for the call stack and new lists
    
    Args:
        L: A list of integers (assumed to be in increasing order)
        
    Returns:
        A new list with elements equal to their indices removed
    """
    def helper(lst, idx=0):
        """
        Inner recursive function with current index tracking.
        
        Args:
            lst: The current list being processed
            idx: The current effective index to check
            
        Returns:
            The processed list with matching elements removed
        """
        if idx >= len(lst):
            # Base case: We've checked all elements
            return lst
        
        if lst[idx] == idx:
            # Remove element and don't increment index
            # (slicing creates a new list combining elements before and after idx)
            return helper(lst[:idx] + lst[idx+1:], idx)
        else:
            # Keep element and move to next
            return helper(lst, idx+1)
    
    return helper(L.copy())  # Use a copy to avoid modifying the original list