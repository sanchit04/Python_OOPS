
#Define a Class
class Item:
    pass

item1=Item() #Instantiating the class or creating an object of class
item1.price = 100 #Instance attribute
item1.quantity = 3 #Instance attribute

print(type(item1)) #<class __main__.Item>
print(type(item1.price)) #<class int>
print(type(item1.quantity)) #<class int>

normal_var1="Hello World" #Creates a variable of type class str
print(type(normal_var1)) # <class 'str'>

#Defining a class with instance method
# Instance method are used to process data passed to the class
# Instance method will always have first argument passed as the object itself

class ItemWithInstanceMethod:

    def calculate_total_price(self,item,price,quantity):
        return f"Total Price of {item} is {price*quantity}"

item2=ItemWithInstanceMethod()
item2.item="Banana"
item2.price=20
item2.quantity=3
#pass instance attributes to instance methods (This are still not instantiated as type of class Item!)
#Only happens when we define using __init__ constructor
print(item2.calculate_total_price(item2.item,item2.price,item2.quantity))

#Direct passing of values of type class str,int,int
print(item2.calculate_total_price("Apple",200,30))
