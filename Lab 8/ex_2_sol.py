def f2_1():
    """
    Reference solution: Implements modular arithmetic with validation.
    
    This solution defines two exception classes and a Modulo class for
    representing and validating modular arithmetic operations.
    """
    class IntError(Exception):
        pass
        
    class PrimeError(Exception):
        pass

    class Modulo:
        def __init__(self, k, p):
            # Validate that p is a prime number
            if not isinstance(p, int) or p < 2\
               or any(p % k == 0 for k in range(2, p // 2 + 1)):
                raise PrimeError(f'{p} is not a prime number')
            # Validate that k is an integer
            if not isinstance(k, int):
                raise IntError(f'{k} is not an integer')
            # Store the modulus and the value
            self.modulus = p
            self.k = k % p

        def __repr__(self):
            return f'Modulo({self.k}, {self.modulus})'

        def __str__(self):
            return f'{self.k} (mod {self.modulus})'
    
    return IntError, PrimeError, Modulo


def f2_2():
    """
    Beginner-friendly version: Implements modular arithmetic with validation
    using detailed comments and simplified logic.
    """
    class IntError(Exception):
        """
        Custom exception class for handling integer-related errors.
        
        Raised when a value that should be an integer is not.
        """
        pass
        
    class PrimeError(Exception):
        """
        Custom exception class for handling prime number related errors.
        
        Raised when a value that should be a prime number is not.
        """
        pass

    class Modulo:
        """
        Class representing a number in modular arithmetic.
        
        In modular arithmetic, numbers "wrap around" after reaching a certain value (the modulus).
        For example, in mod 5, the numbers are 0, 1, 2, 3, 4, and then back to 0.
        
        Attributes:
            modulus (int): The modulus (must be a prime number)
            k (int): The value in the modular system (0 <= k < modulus)
        
        Methods:
            __init__(k, p): Constructor to create a new modular number
            __repr__(): Returns the formal string representation
            __str__(): Returns the human-readable string representation
        """
        def __init__(self, k, p):
            """
            Create a new modular number.
            
            Args:
                k (int): The value in the modular system
                p (int): The modulus (must be a prime number)
                
            Raises:
                PrimeError: When p is not a prime number
                IntError: When k is not an integer
            """
            # Check if p is an integer and at least 2
            if not isinstance(p, int):
                raise PrimeError(f'{p} is not a prime number')
                
            if p < 2:
                raise PrimeError(f'{p} is not a prime number')
            
            # Check if p is a prime number
            # A prime number is only divisible by 1 and itself
            is_prime = True
            for i in range(2, p // 2 + 1):
                if p % i == 0:  # If p is divisible by i, then p is not prime
                    is_prime = False
                    break
            
            if not is_prime:
                raise PrimeError(f'{p} is not a prime number')
            
            # Check if k is an integer
            if not isinstance(k, int):
                raise IntError(f'{k} is not an integer')
            
            # Store the modulus and the value
            # The value is stored as k modulo p (remainder when k is divided by p)
            self.modulus = p
            self.k = k % p

        def __repr__(self):
            """
            Return the formal string representation of the modular number.
            
            This is used for debugging and should ideally be able to recreate the object.
            
            Returns:
                str: A string in the format 'Modulo(k, modulus)'
            """
            return f'Modulo({self.k}, {self.modulus})'

        def __str__(self):
            """
            Return the human-readable string representation of the modular number.
            
            This is used for display purposes.
            
            Returns:
                str: A string in the format 'k (mod modulus)'
            """
            return f'{self.k} (mod {self.modulus})'
    
    return IntError, PrimeError, Modulo


# Test code with automated assertions
def test_modulo_validation():
    """
    Test the Modulo class for various validation scenarios using assertions.
    
    Expected outputs based on the Jupyter Notebook:
    - '1 is not a prime number'
    - '2.0 is not a prime number'
    - '{0} is not an integer'
    - Successful creation of Modulo(6, 11), Modulo(4, 7), and Modulo(16, 29)
    - String representations: '6 (mod 11)', '4 (mod 7)', '16 (mod 29)'
    """
    # Test both implementations
    implementations = [f2_1, f2_2]
    
    for implementation in implementations:
        # Get the classes from the current implementation
        IntError, PrimeError, Modulo = implementation()
        
        # Test case 1: Non-prime modulus (1)
        try:
            Modulo(0, 1)
            assert False, "Should have raised PrimeError for modulus 1"
        except PrimeError as e:
            assert str(e) == "1 is not a prime number", f"Unexpected error message: {e}"
        
        # Test case 2: Non-integer modulus (2.0)
        try:
            Modulo(0, 2.0)
            assert False, "Should have raised PrimeError for modulus 2.0"
        except PrimeError as e:
            assert str(e) == "2.0 is not a prime number", f"Unexpected error message: {e}"
        
        # Test case 3: Non-integer value ({0})
        try:
            Modulo({0}, 11)
            assert False, "Should have raised IntError for value {0}"
        except IntError as e:
            assert str(e) == "{0} is not an integer", f"Unexpected error message: {e}"
        
        # Test case 4: Valid modular numbers
        test_cases = [
            (6, 11, "Modulo(6, 11)", "6 (mod 11)"),
            (4, 7, "Modulo(4, 7)", "4 (mod 7)"),
            (16, 29, "Modulo(16, 29)", "16 (mod 29)")
        ]
        
        for k, p, expected_repr, expected_str in test_cases:
            try:
                m = Modulo(k, p)
                # Check the representations
                assert repr(m) == expected_repr, f"Expected repr '{expected_repr}', got '{repr(m)}'"
                assert str(m) == expected_str, f"Expected str '{expected_str}', got '{str(m)}'"
            except Exception as e:
                assert False, f"Unexpected exception for Modulo({k}, {p}): {e}"
        
        # Test case 5: Value reduction (modulo operation)
        m = Modulo(17, 11)
        assert m.k == 6, f"Expected 17 % 11 = 6, got {m.k}"
        
        # Test case 6: Negative value
        m = Modulo(-5, 11)
        assert m.k == 6, f"Expected -5 % 11 = 6, got {m.k}"
        
        print(f"All tests passed for {implementation.__name__}!")


# Run the test if this file is executed directly
if __name__ == "__main__":
    test_modulo_validation()
