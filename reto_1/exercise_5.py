
from collections import defaultdict
from typing import List

def is_valid_list(str_list: List[str]) -> bool:
    """
    This function checks if a list is valid list 
    of strings.
    
    Parameters:
    str_list (List[str]): The list to check.

    Returns:
    bool: True if all elements are strings, False otherwise.
    
    Raises:
    ValueError: if the input is not a list of strings.

    """

    return (isinstance(str_list, List) and 
            all(isinstance(i, str) for i in str_list)
            )

def filter_anagram_groups(words: List[str]) -> List[str]:
    """

    This function filters and returns words that are anagrams
    from a given list of words.

    Parameters:
    words (List[str]): List of words to check.

    Returns:
    List[str]: List of words that are anagrams.

    Raises:
    ValueError: if the input is not a list of strings.

    Explanation:
    This function has a complexity of O(n*m), where n is the number of words
    and m is the average length of the words.

    In this implementation, we prioritize efficiency by using additional
    memory and assigning a unique prime number to each letter. By leveraging
    the unique factorization property of prime numbers, each word is encoded
    as a product of primes, which allows us to group anagrams efficiently.

    Once the words are grouped, we filter out the groups that contain more
    than one word, since those correspond to valid anagrams.

    It is important to note that this approach can be less practical when
    dealing with very long words, as the product of primes may grow extremely
    large. 


    """

    if not is_valid_list(words):
        raise ValueError("Error: Input must be a valid list of strings.")
    
    primes_correspondence = {
        'a': 2,  'b': 3,  'c': 5,  'd': 7,  'e': 11,
        'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
        'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
        'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
        'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97,
        'z': 101
    }


    groups = defaultdict(list)
    for word in words:
        product = 1
        for char in word:
            product *= primes_correspondence[char]
        groups[product].append(word)

    final_list = []
    for group in groups.values():
        if len(group) > 1:
            final_list.extend(group)

    return final_list

if __name__ == "__main__":
    # Tests
    print(filter_anagram_groups(["amor", "roma", "hola", "aloh", "test"]))
    print(filter_anagram_groups(["rat", "car", "arc", "tar", "elbow", 
        "below", "state", "taste", "cider", "cried", 
        "dusty", "study", "night", "thing", "hello"]
    ))

    # Raises
    try:
        filter_anagram_groups(12345)
    except ValueError as e:
        print(e)
    try:
        filter_anagram_groups(["hello", 123, "world"])
    except ValueError as e:
        print(e)