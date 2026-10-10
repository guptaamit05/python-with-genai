class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.category = category
        self.price = price

    def get_info(self):
        print(
            f"product name: {self.name} \ncategory: {self.category} \nprice: {self.price}"
        )
        print("---" * 10)

    def apply_discount(self, percent):
        discounted_price = self.price - (self.price * percent)
        print(f"Discounted price: {discounted_price:.2f}")
        return discounted_price


product_1 = Product("car", 1000, "four-whiler")
product_2 = Product("bike", 500, "two-whiler")

product_1.get_info()
product_2.get_info()

product_1.apply_discount(0.10)
