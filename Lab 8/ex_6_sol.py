"""
Solution: Implements a circular tuple data structure.

This solution defines a CircularTuple class that behaves like a tuple
but allows indexing beyond its bounds by wrapping around.
"""
from collections.abc import Sequence

class CircularTupleError(Exception):
    """
    Custom exception class for CircularTuple operations.
    
    Raised when attempting to modify a CircularTuple, which should be immutable.
    """
    pass

class CircularTuple(Sequence):
    """
    A sequence that behaves like a tuple but allows circular indexing.
    
    This class inherits from collections.abc.Sequence, which provides
    many sequence methods automatically once __len__ and __getitem__ are implemented.
    
    Attributes:
        L: The underlying sequence (list, tuple, etc.) to wrap
    """
    def __init__(self, L):
        """
        Initialize a CircularTuple with a sequence.
        
        Args:
            L: Any sequence (list, tuple, etc.) to be wrapped
        """
        self.L = L

    def __len__(self):
        """
        Return the length of the CircularTuple.
        
        Returns:
            int: The number of elements in the underlying sequence
        """
        return len(self.L)

    def __getitem__(self, i):
        """
        Get an item from the CircularTuple using circular indexing.
        
        This method allows indexing beyond the bounds of the sequence by
        wrapping around using the modulo operation.
        
        Args:
            i: The index (can be any integer)
            
        Returns:
            The element at the wrapped index
        """
        return self.L[i % len(self)]

    def __setitem__(self, i, x):
        """
        Attempt to set an item in the CircularTuple (not allowed).
        
        This method is implemented to explicitly prevent modification,
        making CircularTuple behave like an immutable sequence.
        
        Args:
            i: The index
            x: The value to set
            
        Raises:
            CircularTupleError: Always raised, as CircularTuple is immutable
        """
        raise CircularTupleError("We could make it work, but we shouldn't!")
