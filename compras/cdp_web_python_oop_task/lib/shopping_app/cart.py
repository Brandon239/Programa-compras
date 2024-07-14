from item_manager import show_items
from wallet import Wallet
from ownable import Ownable
from item import Item

class Cart(Ownable):
    def __init__(self, owner):
        super().__init__()
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("No tienes suficiente dinero en tu billetera")
            return
        
        for item in self.items:
            item.owner.wallet.deposit(item.price)
            self.owner.wallet.withdraw(item.price)
            item.set_owner(self.owner)

        self.items = []
        print("Compra realizada con éxito")

    show_items = show_items
            
