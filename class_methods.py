# class methods are the methods defined with @classmethod in the class and has cls as the default parameter
# (it passes the whole class object instead of individual object which happens in case of self)

class Item:

    discount_rate = 0.8

    def __init__(self,item,price,quantity):
        self.item=item
        self.price=price
        self.quantity=quantity

    # CLASS METHOD USAGE IS SOMETHING WHICH APPLIES AT A GLOBAL LEVEL when I UPDATE DISCOUNT RATE
    # THINK OF IT AS DISCOUNT RATE WILL BE UPDATED FOR ALL ITEMS which will be stored inside our ITEM CLASS STORE
    # CLASS METHODS should be used to update anything for the whole class
    @classmethod
    def update_discount_rate(cls,new_discount_rate):
        cls.discount_rate=new_discount_rate

    def calculate_total_price(self):
        # we are doing self.discount_rate so that at instance level as well we can update the discount rate if needed!
        print(f"Total price for item:{self.item} is {(self.price * self.discount_rate)* self.quantity}")

item1=Item("Apple",20,3)
print(item1.discount_rate) # O/P -> 0.8
# Calling Update Discount rate  class method using instance or class both WORKS!
Item.update_discount_rate(0.6) # Calling class method with a class object is always prefered and considered best practise
#OR
item1.update_discount_rate(0.6) # we updated discount rate for class attribute to 0.3


item1.calculate_total_price() # O/P -> Total price for item:Apple is 30.0

item2 = Item("Banana",20,3)

print(item2.discount_rate)
# O/P -> 0.5 ??? WHY??? class attributes are shared across objects thus when we updated
# class atr in first object to 0.5 even after you instantiate or create new object item2 it will not have
# 0.8 as discount_rate instead it will have 0.5 since its updated
# python checks if item2 instance has discount_rate if it does not have it will check in class level
# in class level it finds discount_rate which is now changed to 0.5

item2.calculate_total_price() # O/P -> Total price for item:Banana is 30.0

# Whenever you want object specific values then we should be using instance attributes
# instead of class attributes which are shared accross all objects

# Instance attributes specific to that instance
# Class attributes shared across all instance/objects