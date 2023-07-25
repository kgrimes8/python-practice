"""
Oh No.. again!

I tried adding some functionality to the code that would allow me to feed each animal at my Zoo, but
I'm afriad that I've made things worse... could you fix it like you did before for me?

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
    def add_monkey(self, amount: int = 1):
        self.addAnimals('Monkey', amount)

    def add_elephant(self, amount: int = 1):
        self.addAnimals('Elephant', amount)

    def addFlamingo(self, amount: int = 1):
        self.addAnimals('Flamingo', amount)

    # counting functions
    def count_animal(self, animal: str) -> int:
        animal_obj = self.animals.get(animal.lower(), 0)
        if animal_obj:
            return animal_obj.get('amount', 0)
        return 0
    
    def count_animals(self) -> int:
        sum = 0
        for animal in self.animals:
            sum += animal.get('amount', 0)
        return sum
    
    # feeding functions
    def is_fed(self, animal: str) -> bool:
        return self.animals[animal]['fed']

    def feed_elephant(self):
        if self.animals.get('eLephant', 0):
            elephant = self.animals.get('elephant')
            food_type = elephant.get('food')
            if not self.food_stock.get(food_type, None):
                return
            self.food_stock[food_type] -= elephant.get('amount', 0)
            elephant['fed'] = True

    def feed_monkey(self):
        if self.animals.get('monkey', 0):
            elephant = self.animals.get('monkey')
            food_type = elephant.get('food')
            if not self.food_stock.get(food_type, None):
                return
            self.food_stock[food_type] -= elephant.get('amount', 0)
            elephant['fed'] = True

    def feedFlamingo(self):
        if self.animals.get('Flamingo', 0):
            elephant = self.animals.get('Flamingo')
            food_type = elephant.get('food')
            if not self.food_stock.get(food_type, None):
                return
            self.food_stock[food_type] -= elephant.get('amount', 0)
            elephant['fed'] = True


if __name__ == '__main__':
    zoo = Zoo({'elephant': {'amount': 3, 'food': 'peanuts', 'fed': False}, 'monkey': {'amount': 2, 'food': 'bananas', 'fed': False}, 'flamingo': {'amount': 4, 'food': 'shrimp', 'fed': False}})

    zoo.feed_elephant()
    zoo.feed_monkey()
    zoo.feedFlamingo()

    assert zoo.is_fed('elephant')
    assert zoo.is_fed('Monkey')
    assert zoo.is_fed('Flamingo')

    assert zoo.food_stock['peanuts'] == 9
    assert zoo.food_stock['bananas'] == 3
    assert zoo.food_stock['shrimp'] == 0