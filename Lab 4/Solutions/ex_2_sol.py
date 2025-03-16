def f2_1(S: set) -> list[set]:
    """
    Creates a list of sets by progressively removing the maximum element from the input set.
    
    Starting with the original set, creates a sequence where each subsequent set
    is derived by removing the maximum element from the previous set.
    
    Args:
        S: A non-empty set of integers
        
    Returns:
        A list of sets, starting with the original set and ending with a set containing
        only the minimum element
    """
    # Create the first element of the result list - a copy of the original set
    U = [set(S)]
    
    # Continue until only one element remains in the set
    while len(S) > 1:
        # Remove the maximum element from the set
        S.remove(max(S))
        # Add a copy of the modified set to the result list
        U.append(set(S))
        
    # Return the list containing all sets
    return U


def f2_2(S: set) -> list[set]:
    """
    Creates a list of sets by iteratively generating subsets of decreasing size.
    
    Uses sorted list approach to create a sequence of sets where each set contains
    only elements less than or equal to a specific threshold.
    
    Args:
        S: A non-empty set of integers
        
    Returns:
        A list of sets, starting with the original set and ending with a set containing
        only the minimum element
    """
    # Sort the elements of the set in descending order
    sorted_elements = sorted(S, reverse=True)
    
    # Initialize the result list
    result = []
    
    # Iterate through each possible subset size
    for i in range(len(sorted_elements)):
        # Create a set with the i smallest elements
        subset = set(sorted_elements[i:])
        # Add this set to our result
        result.append(subset)
        
    # Return the list of sets
    return result


def f2_3(S: set) -> list[set]:
    """
    Creates a list of sets using a recursive approach to generate the sequence.
    
    Recursively builds the list by taking the minimum element and adding progressively
    larger elements to create each subsequent set.
    
    Args:
        S: A non-empty set of integers
        
    Returns:
        A list of sets, starting with the original set and ending with a set containing
        only the minimum element
    """
    # Base case: if set has only one element, return a list with that set
    if len(S) == 1:
        return [S.copy()]
    
    # Find the minimum and maximum elements
    min_element = min(S)
    max_element = max(S)
    
    # Create a new set without the maximum element
    smaller_set = S.copy()
    smaller_set.remove(max_element)
    
    # Recursively generate the list for the smaller set
    result = f2_3(smaller_set)
    
    # Add the original set to the beginning of the result
    result.insert(0, S.copy())
    
    # Return the complete list
    return result