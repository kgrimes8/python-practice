"""
Oh No.. again!

I tried adding some functionality to the code that would allow me to feed each animal at my Zoo, but
I'm afraid that I've made things worse... could you fix it like you did before for me?

You might find there are some errors with my code that you'll need to fix too...
"""

class Zoo:
    def __init__(self, animals = {}):
        self.animals = animals
        self.food_stock = {'peanuts': 10, 'bananas': 4, 'shrimp': 0, 'toast': 1}

    # add animal(s) functions
    def add_animals(self, animal: str, amount: int = 1) -> None:
        animal_obj = self.animals.get(animal.lower(), {})
        animal_obj['amount'] = animal_obj.get('amount', 0) + amount
        self.animals[animal.lower()] = animal_obj

    # functions of default animals to add
    def add_monkey(self, amount: int = 1) -> None:
        self.add_animals('Monkey', amount)

    def add_elephant(self, amount: int = 1) -> None:
        self.add_animals('Elephant', amount)

    def add_flamingo(self, amount: int = 1) -> None:
        self.add_animals('Flamingo', amount)

    # counting functions
    def count_animal(self, animal: str) -> int:
        animal_obj = self.animals.get(animal.lower(), {})
        return animal_obj.get('amount', 0)
    
    def count_animals(self) -> int:
        sum = 0
        for animal in self.animals:
            sum += animal.get('amount', 0)
        return sum
    
    # feeding functions
    def is_fed(self, animal: str) -> bool:
        return self.animals[animal.lower()]['fed']

    def feed_animal(self, animal: str) -> None:
        animal = animal.lower()
        if self.animals.get(animal):
            animal_obj = self.animals.get(animal)
            food_type = animal_obj.get('food')
            if not self.food_stock.get(food_type):
                return
            if self.food_stock[food_type] >= animal_obj.get('amount', 0):
                self.food_stock[food_type] -= animal_obj.get('amount', 0)
                animal_obj['fed'] = True

    def feed_elephant(self):
        self.feed_animal('elephant')

    def feed_monkey(self):
        self.feed_animal('monkey')

    def feed_flamingo(self):
        self.feed_animal('flamingo')


if __name__ == '__main__':
    zoo = Zoo({
        'elephant': {'amount': 3, 'food': 'peanuts', 'fed': False},
        'monkey': {'amount': 2, 'food': 'bananas', 'fed': False},
        'flamingo': {'amount': 4, 'food': 'shrimp', 'fed': False}
        })

    zoo.feed_elephant()
    zoo.feed_monkey()
    zoo.feed_flamingo()

    assert zoo.is_fed('elephant')
    assert zoo.is_fed('Monkey')
    assert not zoo.is_fed('Flamingo')

    assert zoo.food_stock['peanuts'] == 7
    assert zoo.food_stock['bananas'] == 2
    assert zoo.food_stock['shrimp'] == 0