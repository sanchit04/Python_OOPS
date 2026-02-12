from typing import Protocol,runtime_checkable

"""
Protocols rely on type checking which is called as Duck Typing
Duck Typing:In our case Means any Animal that can walk talk eat is considered an Animal
Protocols are type check only they are not enforced at run time like ABCs

If we want to enforce runtime check then 
we should add @runtime_checkable for the class 
and check isinstance of the object is of type protocol class
"""

# Eg of basic protocol:
@runtime_checkable
class Animal(Protocol):
    def walk(self) -> str:
        ...

    def talk(self) -> str:
        ...

    def eat(self) -> str:
        ...

class Kangaroo:

    def __init__(self):
        print("I am Kangaroo!")

    # def walk(self):
    #     return "I run on two legs"

    def talk(self):
        return "I make hmm sound"

    def eat(self):
        return "I eat plants"

class Dog:
    def __init__(self):
        print("I am Dog!")

    def walk(self):
        return "I run on 4 legs"

    def talk(self):
        return "I make bhow sound"

    def eat(self):
        return "I eat chicken"


def define_animal(animal_bio:Animal):
    print("Animal Description")
    print(animal_bio.talk())
    #print(animal_bio.walk())
    print(animal_bio.eat())

if __name__=="__main__":
    dog_bruno = Dog()
    define_animal(dog_bruno) # Here we are directly passing
    # Dog object to a method which needs Animal Object as Parameter.
    """
    #OP:
    I am Dog!
    Animal Description
    I make bhow sound
    I eat chicken
    """

    kangaroo_bro  = Kangaroo()
    define_animal(kangaroo_bro)
    # Here we are directly passing
    # Dog object to a method which needs Animal Object as Parameter.
    # Even if kangaroo is not having the walk method this still works
    # because protocols have no runtime enforcements
    """
    #OP:
    I am Kangaroo!
    Animal Description
    I make hmm sound
    I eat plants
    """
    # below ininstance will work only if we do @runtime_checkable for the class
    # if we dont do that it will give error:
    # TypeError: Instance and class checks can only be used with @runtime_checkable protocols
    assert isinstance(dog_bruno,Animal)
    assert isinstance(kangaroo_bro,Animal) # Kangaroo class
    # is not having the walk method implementation thus it fails in assertion
    #OP:
#     Traceback(most
#     recent
#     call
#     last):
#     File
#     "/Users/sanchitgawde/PycharmProjects/Python_OOPS/protocols_ex.py", line
#     64, in < module >
#     assert isinstance(kangaroo_bro, Animal)
# AssertionError




