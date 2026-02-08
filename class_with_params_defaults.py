
class Item:
    #Adding default of 20 for quantity so now if quantity is not passed while instantiating it still works.
    def __init__(self,item,price,quantity=20):
        self.item=item
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self):
        print(f"Total Price for item:{self.item} is {self.price * self.quantity}")


item1=Item("Apple",200,4)

#This works because default value is set for quantity i.e. 20
item2=Item("Mushroom",30)

item1.calculate_total_price()
item2.calculate_total_price()