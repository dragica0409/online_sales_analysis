class Cart:
    def __init__(self):
        self.cart_items = []  # Lista proizvoda u korpi

    def add_to_cart(self, product):
        """Dodaje proizvod u korpu."""
        self.cart_items.append(product)

    def calculate_total(self):
        """Računanje ukupne vrednosti korpe."""
        total = sum(product.price * product.quantity for product in self.cart_items)
        return f"Ukupna vrednost korpe: {total} RSD"

    def display_cart(self):
        """Prikazuje proizvode u korpi."""
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            for product in self.cart_items:
                print(product.display_info())
