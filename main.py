from product import Product
from product_manager import ProductManager

# Kreiramo instancu ProductManager
manager = ProductManager()

# Dodajemo proizvode
p1 = Product("Laptop", 80000, 5)
p2 = Product("Telefon", 50000, 10)
p3 = Product("Slusalice", 3000, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikazujemo proizvode
print("\nDostupni proizvodi:")
manager.display_products()

# Prikazujemo ukupnu vrednost inventara
print("\n" + manager.total_inventory_value())

