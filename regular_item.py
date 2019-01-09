from item import Item
from updatable import Updatable


class RegularItem(Item,Updatable):

    def setsell_in(self):
        self.sell_in -= 1
        return self.sell_in


    def update_quality(self):
        if sell_in > 0:
            self.quality -= 1
            return self.quality
        else:
            self.quality -= 2
            return self.quality
        setsell_in()

if __name__ == "__main":

    
    pato = RegularItem(pato, 20, 5)
    oca = RegularItem(oca, 0, 5)
    pato.update_quality()
    assert pato.sell_in == 19
    assert pato.update_quality == 4
    assert oca.update_quality == -1
    assert oca.update_quality == 3
