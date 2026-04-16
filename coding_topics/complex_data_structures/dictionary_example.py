class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product_name, quantity):
        if product_name in self.cart:
            self.cart[product_name] += quantity
        else:
            self.cart[product_name] = quantity

    def remove_product(self, product_name):
        if product_name in self.cart:
            del self.cart[product_name]
        else:
            print(f"{product_name} not found in your cart.")

    def show_cart(self):
        if not self.cart:
            print("Your shopping cart it empty.")
        else:
            for product, quantity in self.cart.items():
                print(f"{product}: {quantity}")


if __name__ == "__main__":
    my_cart = ShoppingCart()

    my_cart.add_product("Apples", 5)
    my_cart.add_product("Bananas", 2)
    my_cart.add_product("Apples", 3)

    my_cart.show_cart()

    my_cart.remove_product("Bananas")

    my_cart.show_cart()
