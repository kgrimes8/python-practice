from abc import ABC, abstractmethod


class Bank:
    def __init__(self, owner_inst, value=0):
        if type(owner_inst) is Employee:
            value += 100
        self.balance = float(value)
        self.owner = owner_inst

    def withdraw(self, value):
        if value > 0:
            if self.balance >= value:
                self.balance -= value
            else:
                print("You do not have enough funds.")
        else:
            print("Please enter a valid amount.")

    def deposit(self, value):
        if value > 0:
            self.balance += value
        else:
            print("Please enter a valid amount.")

    def print_balance(self):
        print(f"Your balance is {self.balance}")


class Person(ABC):
    @abstractmethod
    def __init__(self, fname, surname):
        self.fname = fname
        self.surname = surname

    def print_owner(self):
        print(f"{self.fname} {self.surname}")


class Employee(Person):
    def __init__(self, fname, surname, job_title="unknown"):
        super().__init__(fname, surname)
        self.job_title = job_title


class Customer(Person):
    def __init__(self, fname, surname):
        super().__init__(fname, surname)


if __name__ == "__main__":
    pass
