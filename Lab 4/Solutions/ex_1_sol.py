def f1_1(n: int) -> None:
    """
    Prints a sequence for each number from n down to 1.
    
    For each number i, prints the sequence: i, i//2, i//4, ..., 1
    Each integer is printed in a field of width equal to the number of digits in n plus 1.
    
    Uses direct iteration and printing in a loop for concise implementation.
    
    Args:
        n: A positive integer representing the starting number
    """
    # Calculate field width: digits in n plus 1 space
    w = len(str(n)) + 1
    
    # Iterate from n down to 1
    for i in range(n, 0, -1):
        # Store original i to use in the loop since i will be modified
        current = i
        
        # Continue dividing by 2 and printing until we reach 0
        while current:
            # Print the current number with the calculated field width
            print(f'{current:{w}}', end='')
            # Integer division by 2 to get the next number in sequence
            current //= 2
            
        # After printing all numbers in the sequence, move to next line
        print()


def f1_2(n: int) -> None:
    """
    Prints a sequence for each number from n down to 1.
    
    For each number i, prints the sequence: i, i//2, i//4, ..., 1
    Each integer is printed in a field of width equal to the number of digits in n plus 1.
    
    Uses recursive solution with a helper function to generate each sequence.
    
    Args:
        n: A positive integer representing the starting number
    """
    # Calculate field width: digits in n plus 1 space
    width = len(str(n)) + 1
    
    # Helper function to recursively generate a sequence for a number
    def generate_sequence(num):
        # Base case: when num is 0, return empty list
        if num == 0:
            return []
        # Recursive case: current number + sequence for num//2
        return [num] + generate_sequence(num // 2)
    
    # Process each number from n down to 1
    for i in range(n, 0, -1):
        # Get the complete sequence for current number using recursion
        sequence = generate_sequence(i)
        
        # Print each number in the sequence with proper formatting
        for num in sequence:
            print(f'{num:{width}}', end='')
            
        # After printing all numbers in the sequence, move to next line
        print()


def f1_3(n: int) -> None:
    """
    Prints a sequence for each number from n down to 1.
    
    For each number i, prints the sequence: i, i//2, i//4, ..., 1
    Each integer is printed in a field of width equal to the number of digits in n plus 1.
    
    Uses list comprehension and join for string formatting.
    
    Args:
        n: A positive integer representing the starting number
    """
    # Calculate field width: digits in n plus 1 space
    width = len(str(n)) + 1
    
    # Process each number from n down to 1
    for i in range(n, 0, -1):
        # Generate sequence by repeatedly dividing by 2
        num = i
        sequence = []
        while num:
            sequence.append(num)  # Add current number to sequence
            num //= 2             # Divide by 2 to get next number
        
        # Format each number in the sequence with proper width
        formatted_sequence = [f'{num:{width}}' for num in sequence]
        
        # Join all formatted numbers into a single string and print
        print(''.join(formatted_sequence))