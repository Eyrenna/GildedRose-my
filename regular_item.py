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
        getsell_in -= 1
        return getsell_in

    def setquality(self, value):
       if getquality + value > 50:
           getquality = 50
       elif getquality + value >= 0:
           getquality += value
       else:
           getquality = 0


    def update_quality(self):
        if getsell_in > 0:
            getquality -= 1
            return getquality
        else:
            getquality -= 2
            return getquality
        setsell_in()

if __name__ == "__main":

    #CASOS TEST get attributes
    pato = Item("pato", 100, 50)
    assert pato.getname() == "pato"
    assert pato.getsell_in() == 100
    assert pato.getquality() == 50

    #CASOS TEST updatable
    pato = RegularItem(pato, 20, 5)
    oca = RegularItem(oca, 0, 5)
    pato.update_quality()
    assert pato.sell_in == 19
    assert pato.update_quality == 4
    assert oca.update_quality == -1
    assert oca.update_quality == 3


    #CASOS TEST con setquality
    ganso = RegularItem(ganso, 20, 50)
    gansorojo = RegularItem(gansorojo, 20, 0)
    gansoazul = RegularItem(gansoazul, 20, 10)
    assert ganso.update_quality == 50
    assert gansorojo.update_quality == 0
    assert gansoazul.update_quality == 9