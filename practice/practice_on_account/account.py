class Account:

    def __init__(self):
        self._balance = 1000
    def get_balance(self):
       return self._balance

    def make_deposit(self, amount):
        if amount < 0:
            raise ValueError("Invalid Value for Amount.")
        else:
            self._balance += amount


    def make_withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Invalid Value for Amount.")
        else:
            self._balance -= amount