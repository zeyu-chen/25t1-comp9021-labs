def f3_1(n):
    """
    Prints the given number n in all possible bases from the minimum required base to base 10.
    
    This function interprets the string representation of n as a number in different bases,
    and displays what those values would be in decimal (base 10).
    
    Args:
        n: The non-negative integer to convert
    """
    # Convert the number to a string to analyze its digits
    n_as_string = str(n)
    
    # Find the minimum base required:
    # - The base must be at least 2 (binary)
    # - The base must be greater than the largest digit in the number
    # Using set comprehension to get all unique digits as integers
    min_base = max(2, max({int(d) for d in n_as_string}) + 1)
    
    # Iterate through all valid bases from min_base to base 10
    for b in range(min_base, 11):
        # int(n_as_string, b) interprets the string n_as_string as if it were
        # a number written in base b, and returns its decimal (base 10) value
        # For example, int("101", 2) interprets "101" as a binary number and returns 5
        print(f'{n} is {int(n_as_string, b)} in base {b}')


def f3_2(n):
    """
    Prints the given number n in all possible bases from the minimum required base to base 10.
    
    Uses list comprehension for more concise code.
    
    Args:
        n: The non-negative integer to convert
    """
    # Handle special case for 0
    if n == 0:
        for base in range(2, 11):
            print(f"0 is 0 in base {base}")
        return
    
    # Get the string representation of n
    n_str = str(n)
    
    # Find the minimum base required (max digit + 1, at least 2)
    min_base = max(2, max(int(digit) for digit in n_str) + 1)
    
    # Use list comprehension to generate and print all conversions
    [print(f"{n} is {int(n_str, base)} in base {base}") for base in range(min_base, 11)]


def f3_3(n):
    """
    Prints the given number n in all possible bases from the minimum required base to base 10.
    
    Uses functional programming approach with map function.
    
    Args:
        n: The non-negative integer to convert
    """
    # Handle special case for 0
    if n == 0:
        list(map(lambda base: print(f"0 is 0 in base {base}"), range(2, 11)))
        return
    
    # Convert n to string
    n_str = str(n)
    
    # Find the minimum base using functional approach
    min_base = max(2, max(map(int, n_str)) + 1)
    
    # Use map to print each conversion
    list(map(
        lambda base: print(f"{n} is {int(n_str, base)} in base {base}"),
        range(min_base, 11)
    ))


def f3_4(n):
    """
    Prints the given number n in all possible bases from the minimum required base to base 10.
    
    Uses a generator expression approach.
    
    Args:
        n: The non-negative integer to convert
    """
    n_str = str(n)
    
    # For 0, use all bases from 2 to 10
    if n == 0:
        bases = range(2, 11)
    else:
        # Calculate minimum base required
        min_base = max(2, max(int(d) for d in n_str) + 1)
        bases = range(min_base, 11)
    
    # Use generator expression to create each line
    for base in bases:
        yield_value = f"{n} is {int(n_str, base)} in base {base}"
        print(yield_value)


def f3_5(n):
    """
    Prints the given number n in all possible bases from the minimum required base to base 10.
    
    Uses dictionary to track conversions and set for finding max digit.
    
    Args:
        n: The non-negative integer to convert
    """
    n_str = str(n)
    
    # Use set to find unique digits, then find max
    digits = {int(d) for d in n_str}
    
    # Handle empty set (when n is 0)
    if not digits:
        min_base = 2
    else:
        min_base = max(2, max(digits) + 1)
    
    # Dictionary to store converted values
    conversions = {}
    
    # Calculate conversions for each base
    for base in range(min_base, 11):
        conversions[base] = int(n_str, base)
        
    # Print the results
    for base, value in conversions.items():
        print(f"{n} is {value} in base {base}")
