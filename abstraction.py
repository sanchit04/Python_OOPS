#ABSTRACTION EXAMPLE

# Create Item store where we can store items and calculate total price for an item

# Abstraction layer -> Discount Eligibility?
# 1) If Item is apple then we need to apply discount otherwise it should not be applied
# 2) User should not know about which item the discount is applied for

class Item:
    __discount_rate=0.9

    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity


    # Access modifier for apply discount is set to private so that this is not visible at instance level
    def __apply_discount_for_eligible_products(self):
        if self.name.lower()=="apple":
            # Private and protected attributes are accessible inside a class!
            self.price=self.price * Item.__discount_rate

    def calculate_total_price(self):
        # Private and protected methods are accessible inside a class!
        Item.__apply_discount_for_eligible_products(self)
        print(f"Total price for item:{self.name} is {self.price * self.quantity}")


item1=Item("Banana",30,2)
item2=Item("Apple",30,2)

# this does not work since access modifier is private and theres no @property read only set for discount_rate
#item1.discount_rate

#This does not work since modifier is private and theres no way apply discount is accessible
#item1.__apply_discount_for_eligible_products()

# Only accessible method at instance level is calculate total price that's abstraction principle. User should
# know only what is required

item1.calculate_total_price()
item2.calculate_total_price()