class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    # This will be used as base method to calculate total price as a generic item product
    def calculate_total_price(self):
        print(f"Total price for item {self.name} is :{self.price * self.quantity}")

# ItemMetadata inherits all qualities of Item
# It adds its own qualities without having to define qualities of item
class ItemMetadata(Item):

    #Since we need to add two more attributes we are adding category and color and defining in child __init__
    def __init__(self,name,price,quantity,category,color):

        #Super method will be needed when we have defined __init__ in child class if we had not defined __init__
        #bydefault it will go to parent class that is Item
        super().__init__(
            name=name,
            price=price,
            quantity=quantity
        )

        self.category= category
        self.color = color

    def give_stats_about_item(self):
        print(f"Color of Item is {self.color} and it belongs to category:{self.category}")

#Inherits qualities of ItemMetadata which in turn inherits qualities of Item
class Vegetable(ItemMetadata):

    frozen_discount_rate = 0.8

    def __init__(self, name, price, quantity, category, color, is_frozen):

        super().__init__(
            name=name,
            price=price,
            quantity=quantity,
            category = category,
            color=color
        )
        self.is_frozen=is_frozen

    # User can update the frozen discount rate using this class method
    # the new discount rate will be applicable for all the vegetables
    @classmethod
    def update_frozen_discount_rate(cls,updated_rate):
        cls.frozen_discount_rate=updated_rate

    # We are overriding implementation of calculate total price from Item class to match
    # with requirements for category of vegetables

    def calculate_total_price(self):
        #If the vegetable is frozen we apply discount to the price
        if self.is_frozen:
            self.price=Vegetable.frozen_discount_rate * self.price
        print(f"Total price for vegetable:{self.name} is {self.price * self.quantity}")


# We are adding Cucumber to Vegetable category and Item Store
veggie1=Vegetable(name="Cucumber",price=30,quantity=2,category="Vegetable",color="green",is_frozen=True)

#checks if give_stats_about_item is present in instance if not goes and check in vegetable class
#in vegetable class since not present checks it in its parent i.e. ItemMetadata -> able to find it there
veggie1.give_stats_about_item()

#checks if calculate_total_price is present in instance if not goes and check in vegetable class
#in vegetable class its present thus does not traverse back to parent itemmetadata -> parent item
#executes calculate_total_price from vegetable class itself
veggie1.calculate_total_price()

# We are adding apple to item store since theres no personalised implementation for Fruit category
fruit1=ItemMetadata(name="Apple",price=25,quantity=3,category="Fruit",color="red")

#checks if give_stats_about_item is present in instance if not goes and check in ItemMetadata class
#in ItemMetadata class its present
fruit1.give_stats_about_item()

#checks if give_stats_about_item is present in instance if not goes and check in ItemMetadata class
#in ItemMetadata class since not present checks it in its parent i.e. Item -> able to find it there
fruit1.calculate_total_price()

