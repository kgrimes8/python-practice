"""
Oh No! My amazing, excellent, optimal code doesn't work!

Is there any chance you can help me out?
I want to be able to add animals to my Zoo, confirm how many animals there are, and how many types of animals there are.

Add/Edit/Delete any code you see (although I don't see why you would because its clearly perfect).
"""


class Zoo:
    def __init__(self):
        self.monkey = 0
        self.elephant = 0
        self.flamingo = 0

    # add animal(s) functions
    def add_animals(self, animal) -> None:
        animal = animal.lower()
        if animal == "monkey":
            self.monkey += 1
        if animal == "elephant":
            self.elephant += 1
        if animal == "flamingo":
            self.flamingo += 1

    # functions of default animals to add
    def add_monkey(self):
        self.add_animals("monkey")

    def add_elephant(self):
        self.add_animals("elephant")

    def add_flamingo(self):
        self.add_animals("flamingo")

    # counting functions
    def count_animal(self, animal) -> int:
        animal = animal.lower()
        if animal == "monkey":
            return self.monkey
        if animal == "elephant":
            return self.elephant
        if animal == "flamingo":
            return self.flamingo

    def count_animals(self) -> int:
        return sum([self.monkey, self.elephant, self.flamingo])


if __name__ == "__main__":
    zoo = Zoo()

    zoo.add_elephant()
    zoo.add_elephant()
    zoo.add_elephant()

    zoo.add_monkey()
    zoo.add_monkey()

    zoo.add_flamingo()
    zoo.add_flamingo()
    zoo.add_flamingo()
    zoo.add_flamingo()

    assert zoo.count_animal("elephant") == 3
    assert zoo.count_animal("Monkey") == 2
    assert zoo.count_animal("Flamingo") == 4

    assert zoo.count_animals() == 9
