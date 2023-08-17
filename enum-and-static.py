
"""
Enum

An enumeration is a set of symbolic names with a value & can be iterated over.
Enums are great for categories!

Enums are common in several languages & frameworks (including Django) and have many use-cases.
Despite this, they are not Native to Python but I'm including them cause you'll use them at some point. 
"""
from enum import Enum

# Declare an enum like a class which inherits from the 'Enum' class
class CoffeeType(Enum):
    LATTE = 1
    CAPPUCCINO = 2
    AMERICANO = 3
    ESPRESSO = 4
    CORTADO = 5

# Why is this useful? Why do they have numbers?
# Fair questions, remember with our Zoo examples how we kept having to spell "Elephant" and then check 
# whether they were lower case or not - well what if we used an Enum?

class AnimalType(Enum):
    ELEPHANT = 'elephant'
    FLAMINGO = 'flamingo'
    MONKEY = 'monkey'

# in our CoffeeType enum, the numbers are simply an ID so we can identify them - effectively an arbritary value in this use case;
# but with our AnimalType enum, the value is actually a hard-coded string which reduces human-error - imagine the following:

animals = {'elephant': 1}
def count_animal(animal_type: str) -> int:
    return animals.get(animal_type, 0)

# There are plenty of ways for this to go wrong;
count_animal('elephant') # PASS: original method
count_animal('Elephant') # FAIL: capitalised
count_animal('elephanr') # FAIL: typo
count_animal('tiger')    # FAIL: doesn't exist

# but if we specified the function as
def count_animal(animal_type: AnimalType) -> int:
    return animals.get(animal_type.value, 0)         # type.value == the enum's value == 'elephant'
assert count_animal(AnimalType.ELEPHANT) == 1

# that's a lot better, but we can still improve this with one additional change.
# when we set the data to 'elephant' we could actually set it using the enum as well, and then we don't have to rely on the 'value' at all!

animals = {AnimalType.ELEPHANT: 1}
def count_animal(animal_type: AnimalType) -> int:
    return animals.get(animal_type, 0)
assert count_animal(AnimalType.ELEPHANT) == 1

# Now there is no way to mess up what type of animal we are looking for, and if we wanted to add another
# animal, its as simple as updating the AnimalType enum (Also a great way to track what is 'supported' by your application).








"""
Static

A Static method in Python is bound to a class rather than the instances of that class.
This allows static methods to be called without an instance of that class.
However, static methods cannot modify the state of an instance as it is not "bound" to it.

Imagine you were selling coffee, and you wanted to keep track of the number of coffees you had sold.
You cant store that information inside the class, because that would only be available/effected by an instance of that class.

You could create a class to monitor how many coffees you sold, like a TillMachine class, but for simple projects this might be
considered overkill.

What if you wanted to provide some functionality that didn't rely on information about the instance of class? If you don't make 
"""

class Coffee:
    # any variable declared outside of the __init__ function (or not attached to the self object) is static
    # NB: you don't have to start their name with static_<name>
    static_total_sold = 0

    def __init__(self, type: str):
        self.type = type
        # As the variable doesn't belong to a class's instance, self isn't used but instead the class itself is
        Coffee.static_total_sold += 1 # add a new coffee to our counter

    # For functions, we would need to use the '@staticmethod' annotation
    @staticmethod
    def get_total_sold():
        return Coffee.static_total_sold
    
# both these methods work
assert Coffee.static_total_sold == 0
assert Coffee.get_total_sold() == 0

# now everytime we create a coffee instance, our couter will increment
Coffee(CoffeeType.LATTE)
assert Coffee.static_total_sold == 1