#Polymorphism refers to many forms!

class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self):
        print(f"Total price for item:{self.name} is {self.price * self.quantity}")

class Vegetable(Item):
    def __init__(self,name,price,quantity,is_frozen):
        super().__init__(
            name=name,
            price=price,
            quantity=quantity
        )
        if is_frozen:
            discount_rate=0.8
            self.price=self.price*discount_rate

    def calculate_total_price(self):
        extra_discount=0.14
        self.price = self.price * extra_discount
        print(f"Total price for vegetable:{self.name} is {round(self.price * self.quantity,2)}")

# IN OUR EXAMPLE calculate_total_price is returning different outputs
# based on the requirements thus thats the polymorphism principle

item1=Item("Apple",20,3)
item1.calculate_total_price()

veggie1=Vegetable("Cucumber",20,3,True)
veggie1.calculate_total_price()