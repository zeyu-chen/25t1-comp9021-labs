def f6_1(dict_path: str = 'dictionary.txt') -> None:
    """
    Creates a file hierarchy of first 10 words per letter from a dictionary.
    
    The hierarchy structure is:
    - First_10_words_per_letter/ (top directory)
      - Vowels/ (contains files for each vowel: A.txt, E.txt, etc.)
      - Consonants/ (contains files for each consonant: B.txt, C.txt, etc.)
    
    Each letter file contains the first 10 words starting with that letter.
    
    This implementation uses basic file operations and string manipulations.
    
    Args:
        dict_path: Path to the dictionary file (default: 'dictionary.txt')
    """
    import os
    from pathlib import Path
    from string import ascii_uppercase
    
    # Create the top directory
    top_dir = Path('First_10_words_per_letter')
    if not os.path.exists(top_dir):
        os.mkdir(top_dir)
    
    # Create subdirectories for vowels and consonants
    vowels_dir = top_dir / 'Vowels'
    consonants_dir = top_dir / 'Consonants'
    
    if not os.path.exists(vowels_dir):
        os.mkdir(vowels_dir)
    if not os.path.exists(consonants_dir):
        os.mkdir(consonants_dir)
    
    # Process the dictionary file for each letter
    with open(dict_path) as dictionary:
        words = dictionary.readlines()
        
        # Process each uppercase letter
        for letter in ascii_uppercase:
            # Determine the directory based on whether the letter is a vowel
            letter_dir = vowels_dir if letter in 'AEIOUY' else consonants_dir
            
            # Create a file for the current letter
            with open(letter_dir / f'{letter}.txt', 'w') as out_file:
                # Find words starting with the current letter
                count = 0
                for word in words:
                    word = word.strip()
                    if word and word[0].upper() == letter:
                        out_file.write(word + '\n')
                        count += 1
                        if count >= 10:
                            break


def f6_2(dict_path: str = 'dictionary.txt') -> None:
    """
    Creates a file hierarchy of first 10 words per letter from a dictionary.
    
    The hierarchy structure is:
    - First_10_words_per_letter/ (top directory)
      - Vowels/ (contains files for each vowel: A.txt, E.txt, etc.)
      - Consonants/ (contains files for each consonant: B.txt, C.txt, etc.)
    
    Each letter file contains the first 10 words starting with that letter.
    
    This implementation uses dictionary and list comprehensions for a
    more concise approach.
    
    Args:
        dict_path: Path to the dictionary file (default: 'dictionary.txt')
    """
    import os
    from pathlib import Path
    
    # Define letters and their categories
    vowels = 'AEIOUY'
    consonants = 'BCDFGHJKLMNPQRSTVWXZ'
    
    # Create directory structure
    top_dir = Path('First_10_words_per_letter')
    categories = {
        'Vowels': vowels,
        'Consonants': consonants
    }
    
    # Create top directory if it doesn't exist
    os.makedirs(top_dir, exist_ok=True)
    
    # Create category directories and prepare for word collection
    for category, letters in categories.items():
        category_dir = top_dir / category
        os.makedirs(category_dir, exist_ok=True)
    
    # Read all words from dictionary
    with open(dict_path, 'r') as dict_file:
        all_words = [word.strip() for word in dict_file.readlines()]
    
    # Group words by their first letter
    words_by_letter = {}
    for letter in vowels + consonants:
        # Filter words starting with this letter and take first 10
        letter_words = [
            word for word in all_words 
            if word and word[0].upper() == letter
        ][:10]
        words_by_letter[letter] = letter_words
    
    # Write words to files
    for category, letters in categories.items():
        for letter in letters:
            with open(top_dir / category / f'{letter}.txt', 'w') as letter_file:
                letter_file.write('\n'.join(words_by_letter[letter]))
                # Add newline if there are words
                if words_by_letter[letter]:
                    letter_file.write('\n')


def f6_3(dict_path: str = 'dictionary.txt') -> None:
    """
    Creates a file hierarchy of first 10 words per letter from a dictionary.
    
    The hierarchy structure is:
    - First_10_words_per_letter/ (top directory)
      - Vowels/ (contains files for each vowel: A.txt, E.txt, etc.)
      - Consonants/ (contains files for each consonant: B.txt, C.txt, etc.)
    
    Each letter file contains the first 10 words starting with that letter.
    
    This implementation uses a more advanced approach with itertools and
    functional programming concepts.
    
    Args:
        dict_path: Path to the dictionary file (default: 'dictionary.txt')
    """
    import os
    from pathlib import Path
    import itertools
    from collections import defaultdict
    
    # Create directory structure with pathlib
    root_dir = Path('First_10_words_per_letter')
    
    # Define letter categories
    vowels = set('AEIOUY')
    consonants = set('BCDFGHJKLMNPQRSTVWXZ')
    
    # Ensure the directories exist
    root_dir.mkdir(exist_ok=True)
    vowels_dir = root_dir / 'Vowels'
    consonants_dir = root_dir / 'Consonants'
    vowels_dir.mkdir(exist_ok=True)
    consonants_dir.mkdir(exist_ok=True)
    
    # Read words and group by first letter
    def get_words_by_letter():
        """Read dictionary and return words grouped by first letter"""
        words_by_letter = defaultdict(list)
        
        with open(dict_path, 'r') as file:
            for word in file:
                word = word.strip()
                if not word:
                    continue
                
                first_letter = word[0].upper()
                
                # Skip if not an English letter
                if first_letter not in vowels and first_letter not in consonants:
                    continue
                    
                # Only collect the first 10 words for each letter
                if len(words_by_letter[first_letter]) < 10:
                    words_by_letter[first_letter].append(word)
                    
        return words_by_letter
    
    # Get words grouped by first letter
    words_by_letter = get_words_by_letter()
    
    # Write files using generators for better memory efficiency
    def write_letter_file(letter, words):
        """Write words to the appropriate letter file"""
        # Determine the appropriate directory
        directory = vowels_dir if letter in vowels else consonants_dir
        
        # Write words to file
        with open(directory / f'{letter}.txt', 'w') as file:
            file.write('\n'.join(words))
            if words:  # Add final newline if there are words
                file.write('\n')
    
    # Process all letters
    for letter in itertools.chain(vowels, consonants):
        write_letter_file(letter, words_by_letter.get(letter, []))
