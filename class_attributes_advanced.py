# Accessing all the items present in the fruit-store

class Item:
    pay_rate = 0.8
    #Defining an empty list to store all the item objects
    all_tuple = tuple()
    all = []
    print(all_tuple)

    def __init__(self,item,price,quantity):
        self.item=item
        self.price = price
        self.quantity=quantity
        #Appending full instance to the all list
        # so now each time Item class is instantiated the object will be appended to all list
        self.all.append(self)

    # __repr__ magic method is responsible for printing the list objects eg: print(Item.all) or print(item1.all) and
    # by default it will print memory address of each object stored in the list
    # In this case we are changing its default behaviour and printing the actual value
    # def __repr__(self):
    #     return f"Item(item={self.item!r}, price={self.price}, quantity={self.quantity})"
    # Default O/P -> [<__main__.Item object at 0x100633fd0>, <__main__.Item object at 0x100633f10>]

    def __repr__(self):
        return f"Item(item={self.item!r}, price={self.price}, quantity={self.quantity})"

    # __str__ magic method is responsible for printing each object by default prints the memory address of the object
    # eg: print(item1)
    # O/P: <__main__.Item object at 0x1023d7f10>
    # In this case we are changing its default behaviour and printing the actual value

    def __str__(self):
        return f"My values are item={self.item}, price={self.price}, quantity={self.quantity}"

    # IMPORTANT NOTE ABOUT __repr__ and __str__
    # 1) If you have __repr__ defined and there is no __str__ in your class it will affect
    # both list representation as well as individual object representation
    # 2) If you have __str__ defined and there is no __repr__ in your class
    # ONLY individual object representation is affected, LIST will still print memory addresses
    # 3) If you have both __str__ and __repr__ defined then list will be displayed by __repr__
    # individual object will be displayed by __str__


item1=Item("Apple",200,3)
item2=Item("Banana",30,20)

# since uses class level access directly checks in class for the value of all
print(Item.all)
# Op -> [Item(item='Apple', price=200, quantity=3), Item(item='Banana', price=30, quantity=20)]


# End to end working:
# Python checks if item1 object has all defined
# when it see its not defined then it goes to the class
# it finds that its defined in the class and since for each of the object are appeneded to list present in the class
# item1.all shows both item objects
print(item1.all)
# OP -> [Item(item='Apple', price=200, quantity=3), Item(item='Banana', price=30, quantity=20)]

# gives only specific object
print(item1)
# OP -> My values are item=Apple, price=200, quantity=3



