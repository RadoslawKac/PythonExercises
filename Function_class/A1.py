class Pojazd:
    def __init__(self,waga:str,kolor:str) -> None:
        self.waga=waga
        self.kolor=kolor

    @property
    def getwaga(self) -> str:
        return self.waga

    @getwaga.setter
    def setwaga(self,value) -> str:
        self.waga=value

    @property
    def getkolor(self) -> str:
        return self.kolor

    @getkolor.setter
    def setkolor(self,value) -> str:
        self.kolor=value


    def __str__(self) -> str:
        return f"Pojazd o wadze {self.waga} oraz kolorze {self.kolor}"


class Samochod(Pojazd):
    def __init__(self,waga:str,kolor:str,spalanie:str) ->None:
        super().__init__(waga,kolor)
        self.spalanie=spalanie

    @property
    def getspalanie(self) -> str:
        return self.spalanie

    @getspalanie.setter
    def setspalanie(self,value) -> str:
        self.spalanie=value


    def __str__(self) -> str:
       return f"Samochód o wadze {self.waga}, kolorze {self.kolor} oraz spalaniu {self.spalanie}"

p1=Pojazd("2 tony","czarny")
p1.setwaga="3 tony"
print(p1)

s1=Samochod("1 tona","Niebieksi","4.5l/100km")
s1.setwaga = "2 tony"
s1.setspalanie="5l/100km"
print(s1)
