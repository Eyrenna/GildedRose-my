from item import Item
from updatable import Updatable


class RegularItem(Item,Updatable):

    def setsell_in(self):
        self.sell_in -= 1
        return self.sell_in


    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
            return self.quality
        else:
            self.quality -= 2
            return self.quality


if __name__ == "__main":

    
    pato = RegularItem(pato, 20, 5)
    pato.setsell_in()
    pato.update_quality()
    assert pato.sell_in == 19
    assert pato.update_quality == 4
