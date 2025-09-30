from restaurant.bases.menu import MenuItem
from typing import List

class Order:
    """
    Represents a restaurant order containing multiple menu items.
    
    Attributes:
    items (List[MenuItem]): A list of menu items in the order.
    """
    
    def __init__(self):
        """
        Initializes an empty Order instance.
        """
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem):
        """
        Adds a single item to the order.
        
        Parameters:
        item (MenuItem): The menu item to add to the order.
        """
        self.items.append(item)

    def add_items(self, items: List[MenuItem]):
        """
        Adds multiple items to the order.
        
        Parameters:
            items (List[MenuItem]): A list of menu items to add to the order.
        """
        self.items.extend(items)

    def clean_order(self):
        """
        Removes all items from the order, resetting it to an empty state.
        """
        self.items = []

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the order.
        
        Returns:
        float: The total price of the order.
        
        Raises:
        ValueError: If there are no items in the order.
        """
        if not self.items:
            raise ValueError("Error: No items in the order.")
        return sum(item.get_total_price() for item in self.items)

    def apply_discount(self) -> float:
        """
        Calculates the total price with a discount applied.
        
        Applies a 10% discount if the total is greater than $50.
        
        Returns:
        float: The total price after applying the discount.
        
        Raises:
        ValueError: If there are no items in the order (raised by calculate_total).
        """
        total = self.calculate_total()
        if total > 50:
            total *= 0.9
        return total