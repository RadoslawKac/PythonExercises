class Pojazd:
    def __init__(self, kolor, ilosc_kol):
        self.kolor = kolor
        self.ilosc_kol = ilosc_kol

    @property
    def get_kolor(self):
        return self.kolor

    @property
    def get_ilosc_kol(self):
        return self.ilosc_kol

    @get_kolor.setter
    def set_kolor(self, new_kolor):
        self.kolor = new_kolor

    @get_ilosc_kol.setter
    def set_ilosc_kol(self, new_ilosc):
        self.ilosc_kol = new_ilosc

    def wypisz_p(self):
        return f"Kolor: {self.kolor}   Ilosc kol: {self.ilosc_kol}"