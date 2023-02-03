class Liczba:
    wartosc = 0

    def dodaj(self, n):
        self.wartosc += n

    def odejmij(self, n):
        self.wartosc -= n


liczba1 = Liczba()
print(liczba1.wartosc)
liczba1.dodaj(6)
print(liczba1.wartosc)
