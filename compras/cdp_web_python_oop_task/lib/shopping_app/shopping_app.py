from customer import Customer
from item import Item
from seller import Seller


seller = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memory", 13880, seller)
    Item("Motherboard", 28980, seller)
    Item("Power Unit", 8980, seller)
    Item("PC Case", 8727, seller)
    Item("3.5-inch HDD", 10980, seller)
    Item("2.5-inch SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU Cooler", 13400, seller)
    Item("Graphics Card", 23800, seller)


print("🤖 Ingrese su nombre")
customer = Customer(input())

print("🏧 Ingresa la cantidad de dinero que deseas cargar a tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Comenzamos a comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Ingresa el número del producto que deseas")
    number = int(input())

    print("⛏ Ingresa la cantidad de productos que deseas")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Monto total: {customer.cart.total_amount()}")

    print("😭 ¿Deseas finalizar tus compras? (yes/no)")
    end_shopping = input() == "yes"

print("💸 ¿Deseas confirmar tu compra? (yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultados┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ Propiedades de {customer.name}")
customer.show_items()
print(f"😱👛 Saldo de la billetera de {customer.name}: {customer.wallet.balance}")

print(f"📦 Inventario de {seller.name}")
seller.show_items()
print(f"😻👛 Saldo de la billetera de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Monto total: {customer.cart.total_amount()}")

print("🎉 Finaliza la compra")