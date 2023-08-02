"""
Oh No! My amazing, excellent, optimal code doesn't work!

Is there any chance you can help me out?
I want to be able to add animals to my Zoo, confirm how many animals there are, and how many types of animals there are.

Add/Edit/Delete any code you see (although I don't see why you would because its clearly perfect).
"""

def addAnimal(animals: dict, animal: str, number: int = 1) -> dict:
    animal = animal.lower()
    if animal not in animals.keys():
        # TODO can avoid this loop using default dict I think
        animals[animal] = number
    else:
        animals[animal] += number
    return animals

def addElephant(animals: dict):
    return addAnimal(animals, "elephant")

def countAnimal(animals: dict, animal: str):
    return animals[animal.lower()]

def countTypes(animals: dict):
    return len(animals.keys())


def main():

    animals = {}

    # add new animals
    addAnimal(animals, 'Elephant', 2)
    addAnimal(animals, 'Elephant')

    addAnimal(animals, 'monkey', 2)

    addAnimal(animals, 'Flamingo', 4)

    # how many animals are there
    assert countAnimal(animals, 'Elephant') == 3
    assert countAnimal(animals, 'Monkey') == 2
    assert countAnimal(animals, 'Flamingo') == 4


if __name__ == '__main__':
    main()