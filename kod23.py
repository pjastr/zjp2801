class Product:
    def __init__(self, name, price, quality, tax):
        if not isinstance(name, str):
            self.name = ""
        else:
            self.name = name
        if price < 0:
            self.price = 0
        else:
            self.price = price
        self.quality = 0 if quality < 0 else quality
        self.tax = 0 if tax < 0 else tax

    def product_info(self):
        print(f"Info:\nnazwa: {self.name}\ncena: {self.price}\nJakość: {self.quality}\nPodatek: {self.tax} ")


p1 = Product("Jablko", 5.23, 3.4, 0.0)
p1.product_info()
p2 = Product(344, -4, 3, 6)
p2.product_info()
