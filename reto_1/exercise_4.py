

from typing import List

def is_valid_list(nums_list: List[int]) -> bool:
    """
    This function checks if a list is valid list 
    of integers.
    
    Parameters:
    nums_list (List[int]): The list to check.

    Returns:
    bool: True if all elements are integers, False otherwise.
    
    Raises:
    ValueError: if the input is not a list of integers.

    """

    return (isinstance(nums_list, List) and 
            all(isinstance(i, int) for i in nums_list)
            and len(nums_list) > 1
            )

def get_max_sum(nums_list: List[int]) -> int:

    """
    This function returns the maximum sum of
    two consecutive numbers in a list.
    
    Parameters:
    nums_list (List[int]): The list of numbers to check.

    Returns:
    int: The maximum sum of two consecutive numbers.
    
    Raises:
    ValueError: if the input is not a valid list of integers
    with at least two elements.

    Explanation:
    This function has a time complexity of O(n).
    We iterate through the list once, calculating the sum
    of each pair of consecutive numbers and updating the 
    maximum sum found.

    Technically, the algorithm performs two index accesses 
    per iteration, which could be seen as O(2n). However, 
    constant factors are disregarded in asymptotic analysis, 
    so the complexity remains O(n).

    """

    if not is_valid_list(nums_list):
        raise ValueError("Error: Input must be a valid list" \
        " of integers with at least two elements.") 
       
    max_sum = None
    for i in range(len(nums_list) - 1):
        current_sum = nums_list[i] + nums_list[i+1]
        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum

    return max_sum

if __name__ == "__main__":

    # Tests
    print(get_max_sum([2, 4, 7, 9, 11, 12, 13, 15, 17, 18, 
        19, 20, 23, 25, 29, 30, 31, 33, 37, 39]
    ))
    print(get_max_sum([42, 7, 15, 3, 28, 19, 33, 2, 50, 11, 
    8, 25, 39, 6, 47, 13, 20, 29, 5, 37]))

    # Raises
    try:
        get_max_sum(56)
    except ValueError as e:
        print(e)
    try:
        get_max_sum([10, 15, 'hello', 23])
    except ValueError as e:
        print(e)
    try:
        get_max_sum([10])
    except ValueError as e:
        print(e)

   



