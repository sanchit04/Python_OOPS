

class Item:
    #Instantiating instance attributes using __init__ (magic method called only once when instance is created)
    #Takes self as first argument
    def __init__(self,item,price,quantity):
        self.item=item
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self):
        print(f"Total Value for {self.item} is {self.price * self.quantity}")


#instance attributes are passed while instantiating itself since now constructor expects item,price and quantity
#values to be passed while creating the instance
item1=Item("Apple",200,3)
item1.calculate_total_price()

#We can update the instance value like below (Not a good practise!)
item1.price=400
item1.item="Mushroom"

item1.calculate_total_price()
