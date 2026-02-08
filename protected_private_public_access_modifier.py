class Item:
    #Public class attribute can be accessed at instance as well as class level
    pay_rate=0.8

    # Protected (single underscore at start) class attribute can be accessed at instance as well as class level
    # Its the developer responsibility that protected is not accessed at the instance level
    _current_secret="retromusic"

    # Private (double underscore at start) class attribute can be accessed at class level only. There is also a way to access it at Instance Level
    # But its the developer responsibility to not use it

    __hidden_value = "bitcoin"

    # Accessing at class level
    def just_to_test(self):
        print(Item.pay_rate)
        print(Item._current_secret)
        print(Item.__hidden_value)


item1=Item()
item1.just_to_test()

# Accessing at instance level
print(Item.pay_rate)
print(Item._current_secret)
print(Item.__hidden_value)

# O/P ->
# 0.8
# retromusic
# bitcoin
# 0.8
# retromusic
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/Python_Advanced/protected_private_public_access_modifier.py", line 27, in <module>
#     print(Item.__hidden_value)
# AttributeError: type object 'Item' has no attribute '__hidden_value'
