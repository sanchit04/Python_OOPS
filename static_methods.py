# Static methods are the methods which do not pass instance or class object as the first parameter
# @staticmethod is used to define a static method
# used when we want to validate something but not necessary thats totally related to the class
# but still the validation is needed
# can be called at instance or at class level <instanceName>.<static_method> OR <className>.<static_method>

class Item:

    def __init__(self,name,price,quantity):
        # Used validation for name using static method
        if not Item.validate_name(name):
            raise ValueError("Abc is not allowed")

        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def validate_name(name):
        print(name)
        if name == "ABC" or name =="abc":
            print(False)
        else:
            print(True)
        return name!="ABC" and name!="abc"

item1=Item("ABC",20,30)