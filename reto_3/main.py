from restaurant.items import *
from restaurant.orders import Order

if __name__ == "__main__":
    
    # Create a list of different menu items.
    items = [
        Beverage("Large", "Coca-Cola", 2.5, 2),              
        Appetizer(True, "Bruschetta", 4.0, 1),               
        MainCourse("Grilled", "Steak", 18.0, 1),             
        Dessert(True, "Cheesecake", 6.0, 2),                 
        SideDish("Medium", "French Fries", 3.5, 1),          
        Soup(True, "Tomato Soup", 5.0, 3),                   
        Salad("Caesar", "Caesar Salad", 7.0, 1),             
        Sandwich("Whole Wheat", "Chicken Sandwich", 8.0, 2), 
        Pasta("Carbonara", "Spaghetti", 10.0, 1),            
        Pizza("Classic", "Margherita Pizza", 12.0, 2),       
    ]

    # Create an order and add all items
    order = Order()
    order.add_items(items)

    # Calculate and display the total with discount (if applicable)
    try:
        total = order.calculate_total()
        print(f"Total before discount: ${total:.2f}")
        total_after_discount = order.apply_discount()
        print(f"Total after discount: ${total_after_discount:.2f}")
    except Exception as e:
        print(e)

    # Test error handling: attempt to calculate total on an empty order
    try:
        order.clean_order()  
        total_empty = order.calculate_total()  
    except Exception as e:
        print(e)  