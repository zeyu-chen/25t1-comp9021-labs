def f3_1(L: list[list[list[int]]], n: int) -> tuple[list[list[int]], list[list[int]]]:
    """
    Processes a 3-level nested list structure based on specific conditions.
    
    Returns a pair of lists of lists:
    1. First list: For each L' in L with length >= n, collect all positive integers
       from members of L' whose elements sum to a positive number.
    2. Second list: For each L' in L with length >= n and for each L'' in L'
       whose elements sum to a positive number, collect all positive integers from L''.
    
    This implementation uses nested list comprehensions for a concise solution.
    
    Args:
        L: A list of lists of lists of integers
        n: Minimum length requirement for sublists
        
    Returns:
        A tuple of two lists of lists of positive integers
    """
    # First list: For each L1 in L whose length >= n,
    # collect all positive elements from those L2 in L1 whose sum > 0
    first_list = [[e for L2 in L1 if sum(L2) > 0
                     for e in L2 if e > 0
                 ] for L1 in L if len(L1) >= n
                ]
    
    # Second list: For each L1 in L whose length >= n,
    # and for each L2 in L1 whose sum > 0,
    # create a list of all positive elements in L2
    second_list = [[e for e in L2 if e > 0]
                     for L1 in L if len(L1) >= n
                         for L2 in L1 if sum(L2) > 0
                ]
    
    return (first_list, second_list)


def f3_2(L: list[list[list[int]]], n: int) -> tuple[list[list[int]], list[list[int]]]:
    """
    Processes a 3-level nested list structure based on specific conditions.
    
    Returns a pair of lists of lists:
    1. First list: For each L' in L with length >= n, collect all positive integers
       from members of L' whose elements sum to a positive number.
    2. Second list: For each L' in L with length >= n and for each L'' in L'
       whose elements sum to a positive number, collect all positive integers from L''.
    
    This implementation uses multiple simple list comprehensions for improved readability.
    
    Args:
        L: A list of lists of lists of integers
        n: Minimum length requirement for sublists
        
    Returns:
        A tuple of two lists of lists of positive integers
    """
    # First, filter L to only include sublists with length >= n
    filtered_L = [L1 for L1 in L if len(L1) >= n]
    
    # For the first result list:
    # For each filtered L1, collect positive elements from L2 with positive sum
    first_list = []
    for L1 in filtered_L:
        # Create a list of all positive integers from L2s with positive sum
        positives = [e for L2 in L1 if sum(L2) > 0 
                       for e in L2 if e > 0]
        first_list.append(positives)
    
    # For the second result list:
    # For each filtered L1 and each L2 with positive sum,
    # create separate lists of positive elements
    second_list = []
    for L1 in filtered_L:
        for L2 in L1:
            if sum(L2) > 0:
                # Create a list of all positive integers in this L2
                positives = [e for e in L2 if e > 0]
                second_list.append(positives)
    
    return (first_list, second_list)


def f3_3(L: list[list[list[int]]], n: int) -> tuple[list[list[int]], list[list[int]]]:
    """
    Processes a 3-level nested list structure based on specific conditions.
    
    Returns a pair of lists of lists:
    1. First list: For each L' in L with length >= n, collect all positive integers
       from members of L' whose elements sum to a positive number.
    2. Second list: For each L' in L with length >= n and for each L'' in L'
       whose elements sum to a positive number, collect all positive integers from L''.
    
    This implementation uses functional programming techniques with intermediate
    transformations for better structure and readability.
    
    Args:
        L: A list of lists of lists of integers
        n: Minimum length requirement for sublists
        
    Returns:
        A tuple of two lists of lists of positive integers
    """
    # Helper function to get positive elements from a list
    def get_positives(lst: list[int]) -> list[int]:
        return [x for x in lst if x > 0]
    
    # Helper function to check if a list sums to a positive number
    def has_positive_sum(lst: list[int]) -> bool:
        return sum(lst) > 0
    
    # Filter L to only include sublists with length >= n
    qualified_lists = [L1 for L1 in L if len(L1) >= n]
    
    # For the first result, we process each qualified list
    first_result = []
    for L1 in qualified_lists:
        # Collect all positive integers from sublists with positive sum
        all_positives = []
        for L2 in L1:
            if has_positive_sum(L2):
                all_positives.extend(get_positives(L2))
        first_result.append(all_positives)
    
    # For the second result, we create a separate list for each sublist with positive sum
    second_result = []
    for L1 in qualified_lists:
        for L2 in L1:
            if has_positive_sum(L2):
                second_result.append(get_positives(L2))
    
    return (first_result, second_result) 