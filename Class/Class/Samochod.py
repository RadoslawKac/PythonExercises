from Class.pojazd import Pojazd


class Samochod(Pojazd):
    def __init__(self, silnik, przebieg, kolor, ilosc_kol):
        super().__init__(kolor, ilosc_kol)
        self.silnik = silnik
        self.przebieg = przebieg

    @property
    def get_silnik(self):
        return self.silnik

    @property
    def get_przebieg(self):
        return self.przebieg


    @get_silnik.setter
    def set_silnik(self,x):
        self.silnik = x

    @get_przebieg.setter
    def set_przebieg(self,x):
        self.przebieg = x

    def wypisz(self):
        return f"Kolor: {self.kolor}   Ilosc kol: {self.ilosc_kol}   Przebieg: {self.przebieg}   Silnik: {self.silnik}"
