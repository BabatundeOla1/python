from decimal import Decimal

class Account2:
    def __init__(self, name: str, phone_number: str = "00000000000") -> None:
        self.name = name
        self.phone_number = self.set_phone_number(phone_number)
        self.balance = Decimal("0.00")

    def get_pin(self) -> str:
        return self.pin
    def set_phone_number(self, phone_number: str):
        if len(phone_number) != 11:
            raise ValueError("Phone Number must br 11 digit")
        self.phone_number = phone_number
        return self.phone_number

    def get_balance(self) -> Decimal:
        return self.balance

    def get_phone_number(self) -> str:
        return self.phone_number

    def validate_balance(self, amount: Decimal):
        if amount < Decimal("0.00"):
            return "Invalid Balance"
        self.balance = amount
        return self.balance

    def validate_amount(self, amount: Decimal):
        if amount < Decimal("0.00"):
            raise ValueError

    def deposit(self, amount: Decimal):
        self.validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount: Decimal):
        self.validate_amount(amount)
        if amount > self.balance:
            raise ValueError
        self.balance -= amount

    def get_balance(self):
        return self.balance



