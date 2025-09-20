
def calculator(a:float, 
               b:float, 
               operation:str) -> float:

    """
    This function performs basic arithmetic operations.
    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The result of the arithmetic operation.
    
    Raises:
    ValueError: If the operation is not one of '+', '-', '*', '/'.
    ValueError: If division by zero is attempted.
    """

    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ValueError("Error: Division by zero")
        return a / b
    else:
        raise ValueError("Error: Invalid operation. Supported operations are '+', '-', '*', '/'.")

if __name__ == "__main__":

    # Tests
    print(calculator(10, 5, '+'))
    print(calculator(10, 5, '*'))
    print(calculator(10, 5, '-'))
    print(calculator(10, 5, '/'))

    # Raises
    try:
        print(calculator(10, 0, '/'))
    except ValueError as e:
        print(e)
    try:
        print(calculator(10, 5, '^'))
    except ValueError as e:
        print(e)




