

def is_palindrome(word:str) -> bool:

    """
    This function determines if a word is a palindrome.
    Parameters:
    word (str): The word to check.

    Returns:
    bool: True if the word is a palindrome, False otherwise.
    
    Raises:
    ValueError: if the input is not a string.

    Explanation:
    To determine if a word is a palindrome, we only need to check 
    half of the word instead of the entire word.
    The time complexity is still O(n), but this approach 
    is more efficient.

    We compare the characters at the extremes of 
    the word and move inward until we reach the middle.

    """

    if not isinstance(word, str):
        raise ValueError("Error: Input must be a string")
    
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True

if __name__ == "__main__":

    # Tests
    print(is_palindrome("radar"))
    print(is_palindrome("hello"))

    # Raises
    try:
        is_palindrome(12345)
    except ValueError as e:
        print(e)


   



