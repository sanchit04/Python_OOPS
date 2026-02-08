# ENCAPSULATION IS about restricting the user to modify and add new value to instance attributes
# this is done using getters and setters

# below example restricts setting of instance attribute values only once while instantiation

# Good example of Encapsulation :
# item name cannot be updated at instance level. Name will always remain read-only!
# price and quantity can be updated can be updated at instance level using setter
class Item:

    def __init__(self,name,price,quantity):
        # This way we are able to achieve private modifier in python
        # This is not actual private modifier its called name mangling
        self.__name=name
        self.__price=price
        self.__quantity=quantity

    #this will make the name,price and quantity read only and no new values can be set after instantiation
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    #Setter in python will allow setting values to instance attributes even after instantiation

    @quantity.setter
    def quantity(self,quantity):
        if isinstance(quantity,int) and quantity>0:
            self.__quantity=quantity
        else:
            raise ValueError("Quantity has to be a number and should be greater than 0")

    @price.setter
    def price(self,price):
        if isinstance(price,(int,float)) and price>0:
            self.__price=price
        else:
            raise ValueError("Price has to be a number and should be greater than 0")


item1=Item("Apple",20,3)
print(item1.name)
# item1.name = "ABC"
#O/P -> Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/Python_Advanced/encapsulation.py", line 26, in <module>
#     item1.name="ABC"
# AttributeError: can't set attribute


# with setter we can set only price and quantity
item1.price=-0.1
