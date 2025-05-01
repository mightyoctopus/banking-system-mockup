from bank_interface import BankInterface
from bank_account_logic import BankAccount
from data import customers

ba_logic = BankAccount("Mike", 1000)

ui = BankInterface(customers, ba_logic)



