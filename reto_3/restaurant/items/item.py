from restaurant.bases.menu import MenuItem

class Beverage(MenuItem):
    def __init__(self, size: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = size  

class Appetizer(MenuItem):
    def __init__(self, is_vegetarian: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_vegetarian = is_vegetarian

class MainCourse(MenuItem):
    def __init__(self, cooking_style: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cooking_style = cooking_style

class Dessert(MenuItem):
    def __init__(self, has_sugar: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_sugar = has_sugar

class SideDish(MenuItem):
    def __init__(self, portion_size: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portion_size = portion_size  

class Soup(MenuItem):
    def __init__(self, is_hot: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_hot = is_hot

class Salad(MenuItem):
    def __init__(self, dressing: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dressing = dressing  

class Sandwich(MenuItem):
    def __init__(self, bread_type: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bread_type = bread_type 

class Pasta(MenuItem):
    def __init__(self, sauce: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sauce = sauce  

class Pizza(MenuItem):
    def __init__(self, flavor: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flavor = flavor


__all__ = [
    "Beverage",
    "Appetizer",
    "MainCourse",
    "Dessert",
    "SideDish",
    "Soup",
    "Salad",
    "Sandwich",
    "Pasta",
    "Pizza",
]
