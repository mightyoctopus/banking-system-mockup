from data import customers

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.customer_data = customers

    def check_balance(self):
        return self.balance

    def deposit(self, d_amount, name):
        self.customer_data[name]["balance"] += d_amount
        return self.customer_data[name]["balance"]

    def withdrawal(self, w_amount, name):
        balance = self.customer_data[name]["balance"]
        if balance >= w_amount:
            self.customer_data[name]["balance"] -= w_amount
            return True
        else:
            return False





