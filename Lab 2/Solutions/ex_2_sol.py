def f2(text: str) -> str:
    """
    Capitalize words at the beginning of sentences in a text.
    
    This function processes text by:
    1. Capitalizing the first word of the text
    2. Capitalizing any word that follows a sentence-ending punctuation mark (.!?)
    3. Converting all other words to lowercase
    
    Args:
        text (str): The input text to process
        
    Returns:
        str: The processed text with proper sentence capitalization
    """
    # Split the input text into a list of words
    words = text.split()
    
    for i in range(len(words)):
        # If this is the first word in the text OR
        # the previous word ends with a sentence-ending punctuation mark
        if i == 0 or words[i - 1][-1] in ".!?":
            # Capitalize the first letter of the word (title case)
            words[i] = words[i].title()
        else:
            # Otherwise, convert the word to lowercase
            words[i] = words[i].lower()
    
    # Rejoin the processed words with spaces and return the result
    return " ".join(words)

