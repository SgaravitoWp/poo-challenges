

from typing import List

def is_prime(n:int) -> bool:

    """
    
    This function Check if a number is prime.
    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.

    Raises:
    ValueError: if the input is not a positive integer.

    Explanation:
    The complexity of this validation is O(sqrt(n)).
    This implementation is based on a number theory theorem 
    which states that if an integer n is not prime, 
    then it must have a divisor less than or equal to sqrt(n). 
    Therefore, we only need to check for factors in the range 
    from 2 to sqrt(n).

    In addition, we perform three validations before entering 
    the loop. This makes the function more efficient, since 
    it allows us to iterate only through odd numbers.

    
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Error: Input must be a positive integer.")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def extract_primes(nums_list: List[int]) -> List[int]:

    """
    This function extracts prime numbers from a 
    given list of integers.
    
    Parameters:
    nums_list (List[int]): The list of numbers to check.

    Returns:
    List[int]: A list of prime numbers extracted 
    from the input list.
    
    Raises:
    ValueError: if the input is not a list of integers.

    """

    if not isinstance(nums_list, List):
        raise ValueError("Error: Input must be a list.")
    
    prime_numers = filter(lambda x: is_prime(x), nums_list)
    return list(prime_numers)

if __name__ == "__main__":

    # Tests
    print(extract_primes([2, 4, 7, 9, 11, 12, 13, 15, 17, 18, 
        19, 20, 23, 25, 29, 30, 31, 33, 37, 39]
    ))
    print(extract_primes([1, 3, 5, 6, 8, 10, 14, 16, 19, 21, 
    22, 27, 28, 32, 37, 41, 42, 45, 47, 49]))

    # Raises
    try:
        extract_primes(56)
    except ValueError as e:
        print(e)
    try:
        extract_primes([10, 15, 'hello', 23])
    except ValueError as e:
        print(e)


   



