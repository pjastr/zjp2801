class Trip:
    def __init__(self, destination, price):
        self.destination = destination
        self.price = price

    def show_price(self):
        print(f' Price: {self.price}')


trip = Trip(2, 3)
trip.show_price()
