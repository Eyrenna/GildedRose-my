from regular_item import RegularItem


class AgedBrie(RegularItem):


    def update_quality(self):
        if getsell_in >= 0:
            getquality += 1
        else:
            getquality += 2
        setsell_in()



    #CASOS TEST
if __name__ == "__main":
    
    pato = AgedBrie("pato", 2, 0)
    assert pato.update_quality == 1

    oca = AgedBrie("oca", 0, 2)
    assert oca.update_quality == 4