class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Prikazuje informacije o proizvodu."""
        return f"Proizvod: {self.name}, Cena: {self.price} RSD, Količina: {self.quantity}"

    def update_quantity(self, new_quantity):
        """Ažurira količinu proizvoda."""
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Količina ne može biti negativna.")
