
#class name always has to be in camelCase as a good practise
class UntypedItem:
    def __init__(self,item,price,quantity=20):
        self.item=item
        self.price=price
        self.quantity=quantity
    def calculate_total_price(self):
        print(f"Total price for item:{self.item} is {self.price * self.quantity}")

#at this point any type of variable can be passed to our constructor which can give
#wrong results in this case we are passing price as a string instead int in the constructor
item1=UntypedItem("Apple","45")

item1.calculate_total_price()
#O/P -> "45" * 20 -> will print "45" as string for 20 time ->
# Total price for item:Apple is 4545454545454545454545454545454545454545

# we need to restrict such cases this can be handled by typed parameters:
#IMPORTANT: Typed Parameters only shows warning at compile time but no code error
#even if values are passed without any relation to typed parameters

class TypedItem:
    #In this case we are <param_name>:<datatype> thus item will accept only string if its not string it throws warning
    #price will accept only float
    #In case of quantity since we have defaulted to 20 it will always take int
    #if we write quantity as 20.0 it will always take float
    #so when we give default then in that case we dont need to mention the type its implicit
    def __init__(self,item:str,price:float,quantity=20):
        self.item=item
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self):
        print(f"Total price for item:{self.item} is {self.price * self.quantity}")

#This just throws compileTime warning but does not actually restrict working of code
item1=TypedItem("IamWrongItem","65")
item1.calculate_total_price()
#OP -> Total price for item:IamWrongItem is 6565656565656565656565656565656565656565

#To Truly validate the inputs we should use asserts or throw exceptions by implementing a custom logic

class StrongTypedItem:

    def __init__(self,item:str,price:float,quantity=20):

        # asserts if each of the pass param values are instance of the required builtin class of
        # str, float or int
        # For price and quantity it also checks if price and quantity is not a negative number
        # If  not it will throw the error message with AssertionError

        # ASSERTS ARE NOT A GOOD PRACTISE TO DO INPUT VALIDATION since if we do python -0 <main.py>
        # it will disable assertion completely!! assert should be used only for developer validation
        assert isinstance(item,str),"Item can accept only string values"
        # FlOAT OR INT assert OR condition
        assert isinstance(price,(float,int)) and price>0,"price can be a int or float value"
        assert isinstance(quantity,int) and quantity>0,"quantity can be a int only"

        self.item=item
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self):
        print(f"Total price of {self.item} is {self.price * self.quantity}")

#item1=StrongTypedItem(34,"56","7-")

#O/P > assert isinstance(item,str),"Item can accept only string values"
#  AssertionError: Item can accept only string values
# IF assertion Error happens next code of line is not executed!!

item2=StrongTypedItem("apple",45,2)
item2.calculate_total_price()



