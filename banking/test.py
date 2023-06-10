from banking import Bank, Person, Employee, Customer
import unittest
from unittest.mock import patch


class TestBank(unittest.TestCase):
    def test_initial(self):
        owner = Customer("Robyn", "Banks")
        bank = Bank(owner)
        self.assertEqual(bank.balance, 0)

    def test_default_balance(self):
        owner = Customer("Robyn", "Banks")
        bank = Bank(owner, 100)
        self.assertEqual(bank.balance, 100)
        bank = Bank(owner, -100)
        self.assertEqual(bank.balance, -100)

    def test_deposit(self):
        owner = Customer("Robyn", "Banks")
        bank = Bank(owner)
        bank.deposit(100)
        self.assertEqual(bank.balance, 100)

    @patch("builtins.print")
    def test_deposit_value_fault(self, mock_print):
        owner = Customer("Robyn", "Banks")
        bank = Bank(owner)
        bank.deposit(0)
        mock_print.assert_called_with("Please enter a valid amount.")
        bank.deposit(-10)
        mock_print.assert_called_with("Please enter a valid amount.")

    def test_withdraw(self):
        owner = Customer("Robyn", "Banks")
        bank = Bank(owner, 100)
        bank.withdraw(50)
        self.assertEqual(bank.balance, 50)

    @patch("builtins.print")
    def test_withdraw_value_fault(self, mock_print):
        owner = Customer("Robyn", "Banks")
        bank = Bank(owner, 100)
        bank.withdraw(200)
        mock_print.assert_called_with("You do not have enough funds.")
        bank.withdraw(-10)
        mock_print.assert_called_with("Please enter a valid amount.")
        bank.withdraw(0)
        mock_print.assert_called_with("Please enter a valid amount.")

    @patch("builtins.print")
    def test_print_balance(self, mock_print):
        owner = Customer("Robyn", "Banks")
        bank = Bank(owner)
        bank.print_balance()
        mock_print.assert_called_with("Your balance is 0.0")


class TestPerson(unittest.TestCase):
    def test_person_abstract(self):
        with self.assertRaises(TypeError):
            Person("Robyn", "Banks")


class TestEmployee(unittest.TestCase):
    def test_initial(self):
        employee = Employee("Robyn", "Banks")
        self.assertEqual(employee.job_title, "unknown")
        self.assertEqual(employee.fname, "Robyn")

    @patch("builtins.print")
    def test_super_inheritance(self, mock_print):
        employee = Employee("Robyn", "Banks")
        employee.print_owner()
        mock_print.assert_called_with("Robyn Banks")


class TestCustomer(unittest.TestCase):
    @patch("builtins.print")
    def test_initial(self, mock_print):
        customer = Customer("Robyn", "Banks")
        customer.print_owner()
        mock_print.assert_called_with("Robyn Banks")


class TestEmployeeBonus(unittest.TestCase):
    def test_employee_bonus(self):
        employee = Employee("Robyn", "Banks")
        bank = Bank(employee)
        self.assertEqual(bank.balance, 100)
        customer = Customer("Robyn", "Banks")
        bank = Bank(customer)
        self.assertEqual(bank.balance, 0)


if __name__ == "__main__":
    unittest.main()
