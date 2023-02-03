class Rectangle:
    width = 20
    heigth = 30

    def square(self):
        return self.width * self.heigth

    def length(self):
        return 2 * self.width + 2 * self.heigth

    def show_width(self):
        return self.width

    def show_square(self):
        print(f'Pokazuje pole {self.square()}')


rect = Rectangle()
print(rect.square())
rect.show_square()
