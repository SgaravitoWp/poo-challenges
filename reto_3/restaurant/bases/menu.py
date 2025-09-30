class MenuItem:
    """
    Represents an item in a restaurant menu.
    
    Attributes:
    name (str): The name of the menu item.
    price (float): The price of a single unit of the item.
    quantity (int): The number of units ordered.
    """
    
    def __init__(self, 
                 name: str, 
                 price: float,
                 quantity: int = 1):
        """
        Initializes a MenuItem instance.
        
        Parameters:
        name (str): The name of the menu item.
        price (float): The price of a single unit of the item.
        quantity (int): The number of units ordered. Default is 1.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self) -> float:
        """
        Calculates the total price for the menu item.
        
        Returns:
        float: The total price (price multiplied by quantity).
        """
        return self.price * self.quantity