
class Item:
    #Class attribute the variable which is defined at a class level
    pay_rate=0.8

    def __init__(self,item,price,quantity):
        self.item=item
        self.price=price
        self.quantity=quantity

    def apply_discount(self):
        # below way cannot be used and will result an error pay_rate cannot be accessed like this
        #self.price=self.price * pay_rate

        # To access payrate we need to do: className.<class_attribute_name> or can do self.<class_attribute_name>
        # className.<class_attribute_name> -> Will always apply class level value only no modifications at instance level
        # will be considered
        # self.price=self.price * Item.pay_rate

        # self.<class_attribute_name> -> Allows modification at instance level
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        print(f"Total price for {self.item} after discount is :{self.price * self.quantity}")

item1=Item("Apple",30,2)


#in this case we are trying to set pay_rate at an instance level so that for each item we can apply
#different discount rate eg Apple can have 20% discount, bananas can have 10% discount etc
item1.pay_rate=0.9

# Here the discount is applied
item1.apply_discount()

# Calculate the total price after discount
item1.calculate_total_price()
#O/P-> Total price for Apple after discount is :48.0 - ? Event after setting 0.9 as pay_rate at instance level
# we still see class level value being used which is 0.8 that is because we are applying
# discount based on Item.pay_rate (this will always consider class level value only)
# if we want to allow instance level modification then we should use self.pay_rate while applying discount

print(f"Class-Level Pay_Rate:{Item.pay_rate}")
print(f"Instance-Level Pay_Rate:{item1.pay_rate}")

#IMPORTANT:
# __dict__ is a magic method which return a dictionary with all key details about the class or of the instance/object
# below is for class
print(f"All attribute of class:{Item.__dict__}")
# Output> All attribute of class:{'__module__': '__main__', 'pay_rate': 0.8,
# '__init__': <function Item.__init__ at 0x102c3f940>,
# 'apply_discount': <function Item.apply_discount at 0x102c3f9d0>,
# 'calculate_total_price': <function Item.calculate_total_price at 0x102c3fa60>,
# '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>,
# '__doc__': None}

#below is for an instance
print(f"All attribute of instance:{item1.__dict__}")
# Output> All attribute of instance:{'item': 'Apple', 'price': 27.0, 'quantity': 2, 'pay_rate': 0.9}