# Assume that the arguments first_terms and factors are two nonempty
# lists of the same length consisting of integers or floating point
# numbers, and that the argument n is an integer at least equal to 0
# and at most equal to 997 + n (limited by the recursion depth).
#
# Writing first_terms as (x_0, ..., x_k) and factors as (a_0, ..., a_k),
# returns the term of index n of the series (x_i), i >= 0, such that for all
# j > k, x_j = a_0 * x_{j-k-1} + a_1 * x_{j-k} + ... + a_k * x_{j-1}.

from typing import List, TypeVar

# Define a type for numbers (integers or floats)
Number = TypeVar('Number', int, float)

def f6_1(first_terms: List[Number], factors: List[Number], n: int) -> Number:
    """
    Calculates the nth term of a recursively defined sequence using memoization.

    This implementation uses the original recursive approach with memoization to
    efficiently calculate the nth term of the sequence defined by:
    - Initial terms: first_terms = [x_0, x_1, ..., x_k]
    - Recurrence relation: x_j = a_0 * x_{j-k-1} + a_1 * x_{j-k} + ... + a_k * x_{j-1}
      for j > k, where factors = [a_0, a_1, ..., a_k]

    Args:
        first_terms: A list of initial terms of the sequence [x_0, x_1, ..., x_k]
        factors: A list of coefficients [a_0, a_1, ..., a_k] for the recurrence relation
        n: The index of the term to calculate (0-based indexing)

    Returns:
        The nth term of the sequence

    Example:
        f6_1([0, 1], [1, 1], 10) returns 55 (the 10th Fibonacci number)
    """
    # Initialize the series with the first terms
    series = {i: first_terms[i] for i in range(len(first_terms))}

    # Define the helper function for recursive calculation with memoization
    def _calculate_term(idx: int) -> None:
        """
        Recursively calculates terms of the sequence and stores them in the series dictionary.

        Args:
            idx: The index of the term to calculate
        """
        # If the term is already calculated, return
        if idx in series:
            return
        # Calculate the term using the recurrence relation
        result = 0
        for i in range(1, len(factors) + 1):
            # Recursively calculate the required previous terms
            _calculate_term(idx - i)
            # Apply the recurrence relation
            result += factors[-i] * series[idx - i]
        # Store the result in the series dictionary
        series[idx] = result

    # Call the helper function to calculate the nth term
    _calculate_term(n)
    # Return the nth term
    return series[n]
