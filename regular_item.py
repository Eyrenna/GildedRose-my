from item import Item
from updatable import Updatable


class RegularItem(Item,Updatable):

    def getsell_in(self):
        return self.sell_in


    def getquality(self):
        return self.quality
    
    def getname(self): 
        return self.name


    def setsell_in(self):
        self.sell_in -= 1

    def setquality(self, value):
       if self.quality + value > 50:
           self.quality = 50
       elif self.quality + value >= 0:
           self.quality += value
       else:
           self.quality = 0


    def update_quality(self):
        if self.sell_in > 0:
            self.quality -=1
        else:
            self.quality -= 2
        self.setsell_in()

if __name__ == "__main__":

    #CASOS TEST get attributes
    pato = RegularItem("pato", 100, 50)
    assert pato.getname() == "pato"
    assert pato.getsell_in() == 100
    assert pato.getquality() == 50

    #CASOS TEST updatable
    pato = RegularItem("pato", 20, 5)
    oca = RegularItem("oca", 0, 5)
    pato.update_quality()
    oca.update_quality()
    assert pato.sell_in == 19
    assert pato.quality == 4
    assert oca.sell_in == -1
    assert oca.quality == 3


    #CASOS TEST con setquality
    ganso = RegularItem("ganso", 20, 50)
    gansorojo = RegularItem("gansorojo", 20, 0)
    gansoazul = RegularItem("gansoazul", 20, 10)
    assert ganso.quality == 50
    assert gansorojo.quality == 0
    assert gansoazul.quality == 9