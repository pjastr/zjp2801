class Rectangle:
    width = 0
    height = 0

    def add_parameters(self, x, y):
        self.width = x
        self.height = y

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def info(self):
        print(f"Szerokość: {self.width}, Wysokość: {self.height}, Pole: {self.area()}, Obwód: {self.perimeter()}")


rect1 = Rectangle()
rect1.add_parameters(20, 30)
rect1.info()
