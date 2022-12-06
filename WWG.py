import random

gib1 = ["orfle", "gar", "shmoo", "oof", "tiac", "le", "bop", "usa", "boo", "fle", "ifl", "ifle", "wok", "ok", "tion", "rad", "orph", "orphy", "er", "onk", "gon", "gig", "barf", "fer", "inkl", "unkl", "per"]
gib2 = ["arka", "oing", "zoi", "quarf", "qu", "arf", "ank", "len", "bl", "bong", "ong", "oi", "doi", "an", "bul", "fim", "wop", "sem", "ex", "exp", "lorat", "ion", "rut", "oob", "onk", "obl"]
gib3 = ["go", "id", "aba", "loo", "oo", "o", "pl", "ean", "tes", "uttle", "phy", "dale", "sy", "erg", "ow", "qwert", "quan"]

def gibber():
    one = gib1[random.randint(0, 26)]
    two = gib2[random.randint(0, 25)]
    three = gib2[random.randint(0, 12)]

    output = one + two + three
    return output

if __name__ == "__main__":
    print(gibber())
    print(gibber())
    print(gibber())
    print(gibber())
    print(gibber())














