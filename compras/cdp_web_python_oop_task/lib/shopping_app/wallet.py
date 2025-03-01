
class Wallet:
    def __init__(self, owner):
        self.set_owner(owner)
        self.balance = 0

    def set_owner(self, owner):
        self.owner = owner

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if self.balance < amount:
            return  None
        self.balance -= int(amount)
        return amount