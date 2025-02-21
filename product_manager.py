from product import Product

class ProductManager:
    def __init__(self):
        self.products = []  # Lista svih proizvoda

    def add_product(self, product):
        """Dodaje novi proizvod u listu."""
        self.products.append(product)

    def display_products(self):
        """Prikazuje sve proizvode u inventaru."""
        if not self.products:
            print("Nema dostupnih proizvoda.")
        else:
            for product in self.products:
                print(product.display_info())

    def total_inventory_value(self):
        """Izračunava ukupnu vrednost svih proizvoda u inventaru."""
        total_value = sum(product.price * product.quantity for product in self.products)
        return f"Ukupna vrednost inventara: {total_value} RSD"

def remove_product(self, product_name):
    """Uklanja proizvod iz liste na osnovu imena."""
    for product in self.products:
        if product.name == product_name:
            self.products.remove(product)
            print(f"Proizvod '{product_name}' je uklonjen.")
            return
    print(f"Proizvod '{product_name}' nije pronađen.")
