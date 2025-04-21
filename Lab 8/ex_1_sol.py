def f1_1():
    """
    Reference solution: Implements a prime number validation and storage class.
    """
    from math import sqrt

    class PrimeError(Exception):
        pass

    class Prime:
        primes = set()

        def reset():
            Prime.primes = set()

        def __init__(self, p):
            if not isinstance(p, int) or p < 2\
               or any(p % k == 0 for k in range(2, round(sqrt(p)) + 1)):
                raise PrimeError(f'{p} is not a prime number')
            if p in Prime.primes:
                raise PrimeError(f'We have seen {p} before')
            Prime.primes.add(p)

    return PrimeError, Prime


def f1_2():
    """
    Beginner-friendly version: Implements a prime number validation and storage class
    with detailed comments and simplified logic.
    """
    from math import sqrt

    class PrimeError(Exception):
        """
        Custom exception class for handling prime number related errors.

        Raised when the input is not a prime number or has been added before.
        """
        pass

    class Prime:
        """
        Prime number class for validating and storing prime numbers.

        Attributes:
            primes (set): Class variable to store all prime numbers that have been created

        Methods:
            reset(): Static method to reset the set of stored prime numbers
            __init__(p): Constructor to validate and store a new prime number
        """
        # Class variable to store all prime numbers that have been created
        primes = set()

        @staticmethod
        def reset():
            """
            Reset the set of stored prime numbers.

            Call this method when you need to clear all stored prime numbers.
            """
            Prime.primes = set()

        def __init__(self, p):
            """
            Create a new prime number instance.

            Args:
                p: The value to validate and store

            Raises:
                PrimeError: When the input is not an integer, less than 2,
                           not a prime number, or has been added before
            """
            # Check if the input is an integer and at least 2
            if not isinstance(p, int):
                raise PrimeError(f'{p} is not a prime number')

            if p < 2:
                raise PrimeError(f'{p} is not a prime number')

            # Check if the input is a prime number
            # Only need to check up to sqrt(p) because if p has a factor,
            # at least one of them is less than or equal to sqrt(p)
            is_prime = True
            for k in range(2, int(sqrt(p)) + 1):
                if p % k == 0:  # If p is divisible by k, then p is not prime
                    is_prime = False
                    break

            if not is_prime:
                raise PrimeError(f'{p} is not a prime number')

            # Check if the input has been added before
            if p in Prime.primes:
                raise PrimeError(f'We have seen {p} before')

            # Add the validated prime number to the set
            Prime.primes.add(p)

    return PrimeError, Prime


# Test code with automated assertions
def test_prime_validation():
    """
    Test the Prime class for various validation scenarios using assertions.

    This function tests both implementations (f1_1 and f1_2) to ensure they behave identically.
    """
    # Test both implementations
    implementations = [f1_1, f1_2]

    for implementation in implementations:
        # Get the classes from the current implementation
        PrimeError, Prime = implementation()

        # Reset the Prime class before testing
        Prime.reset()

        # Test case 1: Non-prime number (1)
        try:
            Prime(1)
            assert False, "Should have raised PrimeError for 1"
        except PrimeError as e:
            assert str(e) == "1 is not a prime number", f"Unexpected error message: {e}"

        # Test case 2: Non-integer (2.0)
        try:
            Prime(2.0)
            assert False, "Should have raised PrimeError for 2.0"
        except PrimeError as e:
            assert str(e) == "2.0 is not a prime number", f"Unexpected error message: {e}"

        # Test case 3: Non-number object ([1, 2, 3])
        try:
            Prime([1, 2, 3])
            assert False, "Should have raised PrimeError for [1, 2, 3]"
        except PrimeError as e:
            assert str(e) == "[1, 2, 3] is not a prime number", f"Unexpected error message: {e}"

        # Test case 4: Valid prime (2)
        try:
            Prime(2)
        except Exception as e:
            assert False, f"Unexpected exception for valid prime 2: {e}"

        # Test case 5: Duplicate prime (2 again)
        try:
            Prime(2)
            assert False, "Should have raised PrimeError for duplicate 2"
        except PrimeError as e:
            assert str(e) == "We have seen 2 before", f"Unexpected error message: {e}"

        # Test case 6: Non-prime number (4)
        try:
            Prime(4)
            assert False, "Should have raised PrimeError for 4"
        except PrimeError as e:
            assert str(e) == "4 is not a prime number", f"Unexpected error message: {e}"

        # Test case 7: Valid prime (5)
        try:
            Prime(5)
        except Exception as e:
            assert False, f"Unexpected exception for valid prime 5: {e}"

        # Test case 8: Duplicate prime (2 again)
        try:
            Prime(2)
            assert False, "Should have raised PrimeError for duplicate 2"
        except PrimeError as e:
            assert str(e) == "We have seen 2 before", f"Unexpected error message: {e}"

        # Test case 9: Duplicate prime (5 again)
        try:
            Prime(5)
            assert False, "Should have raised PrimeError for duplicate 5"
        except PrimeError as e:
            assert str(e) == "We have seen 5 before", f"Unexpected error message: {e}"

        print(f"All tests passed for {implementation.__name__}!")


# Run the test if this file is executed directly
if __name__ == "__main__":
    test_prime_validation()