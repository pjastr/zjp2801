class Rectangle:
    width = 1
    height = 1

    def kwadrat(self, a=width, b=height):
        self.width = a
        self.height = b
        print(f"szerokość = {self.width}")
        print(f'wysokość = {self.height}')
        print(f'Pole = {self.width * self.height}')
        print(f'obwód = {self.width * 2 + self.height * 2}')


kwadrat1 = Rectangle()
kwadrat1.kwadrat()
