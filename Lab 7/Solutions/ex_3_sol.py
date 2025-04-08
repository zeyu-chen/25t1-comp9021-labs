# Assume that the argument L is a list of integers.
#
# - If L has a first element n1, then outputs n lines of Xs
#   (lines of rank 1).
# - If L has a second element n2, then outputs between 2 lines
#   of rank 1 n2 lines of Xs preceded by a tab (lines of rank 2).
# - If L has a third element n3, then outputs between 2 lines
#   of rank 2 n3 lines of Xs preceded by two tabs (lines of rank 3).
# ...
#
# The output is printed out, not returned.

from typing import List

def f3_1(L: List[int]) -> None:
    """
    Prints a hierarchical pattern of 'X' characters based on the input list.
    
    This implementation uses recursion to generate the nested structure:
    - For each element L[n] in the list, prints L[n] lines of 'X' characters
      preceded by n tabs
    - The lines are arranged in a nested pattern where higher rank lines
      (with more tabs) are placed between lower rank lines
    
    Args:
        L: A list of integers where each element determines the number of 'X's
           to print at that nesting level
    
    Example:
        f3_1([2, 1]) would print:
        X
        \tX
        X
    """
    # Helper function to handle the recursive pattern generation
    def _f3_1(L: List[int], n: int) -> None:
        """
        Recursive helper function that handles the nested printing pattern.
        
        Args:
            L: The input list of integers
            n: The current index in the list (also determines the indentation level)
        """
        # Base case: if we've processed all elements in the list, return
        if n == len(L):
            return
            
        # Print all but the last 'X' at the current level, with nested calls
        for _ in range(L[n] - 1):
            print('\t' * n + 'X')
            _f3_1(L, n + 1)
            
        # Print the last 'X' at the current level if L[n] > 0
        if L[n]:
            print('\t' * n + 'X')
    
    # Start the recursion with the first element (index 0)
    _f3_1(L, 0)


def f3_2(L: List[int]) -> None:
    """
    Prints a hierarchical pattern of 'X' characters based on the input list.
    
    This implementation uses an iterative approach with a stack to simulate
    the recursion, which can be more efficient for very deep nesting levels
    as it avoids potential stack overflow issues.
    
    Args:
        L: A list of integers where each element determines the number of 'X's
           to print at that nesting level
    
    Example:
        f3_2([2, 1]) would print:
        X
        \tX
        X
    """
    # Handle empty list case
    if not L:
        return
        
    # Initialize stack with starting state: (level, count)
    # level: current index in L (also the indentation level)
    # count: how many X's still to print at this level
    stack = [(0, L[0])]
    
    while stack:
        level, count = stack[-1]
        
        # If we've printed all X's at this level, pop and continue
        if count == 0:
            stack.pop()
            continue
            
        # Print an X at the current level
        print('\t' * level + 'X')
        
        # Decrement the count for this level
        stack[-1] = (level, count - 1)
        
        # If there are more levels, and we're not at the last X of this level,
        # push the next level onto the stack
        if level + 1 < len(L) and count > 1:
            stack.append((level + 1, L[level + 1]))