class Item():
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def getname(self): 
        return self.name
    
    def getsell_in(self):
        return self.sell_in

    def getquality(self):
        return self.quality


if __name__ == "__main__":
    pato = Item("pato", "100", "50")
    assert pato.getname() == "pato"
    assert pato.getsell_in() == "100"
    assert pato.getquality() == "50"