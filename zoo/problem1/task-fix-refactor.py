"""
Oh No! My amazing, excellent, optimal code doesn't work!

Is there any chance you can help me out?
I want to be able to add animals to my Zoo, confirm how many animals there are, and how many types of animals there are.

Add/Edit/Delete any code you see (although I don't see why you would because its clearly perfect).
"""


animals = {}


def addMonkey():
    animals['Monkey'] = animals['Monkey'] + 1


def addElephant():
    animals['Elephant'] = animals['Elephant'] + 1


def addFlamingo():
    animals['Flamingo'] = animals['Flamingo'] + 1


def countAnimal(animal: str):
    return animals[animal]


def main():
    # add new animals
    addElephant()
    addElephant()
    addElephant()

    addMonkey()
    addMonkey()

    addFlamingo()
    addFlamingo()
    addFlamingo()
    addFlamingo()

    # how many animals are there
    assert countAnimal('Elephant') == 3
    assert countAnimal('Monkey') == 2
    assert countAnimal('Flamingo') == 4


if __name__ == '__main__':
    main()