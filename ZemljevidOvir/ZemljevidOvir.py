import unittest
def dolzina_ovir(vrstica):
    dolzinaOvire = 0
    for znak in vrstica:
        if znak == "#":
            dolzinaOvire += 1
    return dolzinaOvire

def stevilo_ovir(vrstica):
    steviloOvir = 0
    trenutnaOvira = 0
    for znak in vrstica:
        if znak == "#":
            trenutnaOvira += 1
        else:
            if trenutnaOvira >= 1:
                steviloOvir += 1
            trenutnaOvira = 0
    if trenutnaOvira >= 1:
        steviloOvir += 1
    return steviloOvir

def najsirsa_ovira(vrstica):
    najsirsaOvira = 0
    trenutnaOvira = 0
    for znak in vrstica:
        if znak == "#":
            trenutnaOvira += 1
        else:
            if trenutnaOvira > najsirsaOvira:
                najsirsaOvira = trenutnaOvira
            trenutnaOvira = 0
    if trenutnaOvira > najsirsaOvira:
        najsirsaOvira = trenutnaOvira
    return najsirsaOvira

def pretvori_vrstico(vrstica):
    ovire = []
    trenutnaOvira = None
    index = 1
    for znak in vrstica:
        if znak == "#":
            if trenutnaOvira is None:
                trenutnaOvira = (index, index)
            else:
                trenutnaOvira = (trenutnaOvira[0], index)
        else:
            if trenutnaOvira is not None:
                ovire.append(trenutnaOvira)
                trenutnaOvira = None
        index += 1
    if trenutnaOvira is not None:
        ovire.append(trenutnaOvira)
    return ovire

def pretvori_zemljevid(vrstice):
    ovire = []
    y = 1
    for vrstica in vrstice:
        for x0, x1 in pretvori_vrstico(vrstica):
            ovire.append((x0, x1, y))
        y += 1
    return sorted(ovire, key=lambda x: (x[2], x[0])) #sortirano po vrsticah in stolpcih

def izboljsave(prej, potem):
    pretvoriPrej = pretvori_zemljevid(prej) #pretvorimo v seznam trojk
    pretvoriPotem = pretvori_zemljevid(potem) #pretvorimo v seznam trojk
    noveOvire = []
    for nova_ovira in pretvoriPotem: #zanka skozi sezname trojk potem
        if nova_ovira not in pretvoriPrej: #če sezname trojk potem ni v seznamih trojk prej, potem je to nova ovira
            noveOvire.append(nova_ovira)
    return sorted(noveOvire, key=lambda x: (x[2], x[0])) #sortirano po vrsticah in stolpcih

def huligani(prej, potem):
    noveOvire = izboljsave(prej, potem)
    odstranjeneOvire = []
    pretvoriPrej = pretvori_zemljevid(prej)
    pretvoriPotem = pretvori_zemljevid(potem)
    for oviraPrej in pretvoriPrej: #zanka skozi sezname trojk potem
        if oviraPrej not in pretvoriPotem: #če sezname trojk prej ni v seznamih trojk potem, potem je to odstranjena ovira
            odstranjeneOvire.append(oviraPrej)
    return (sorted(noveOvire, key=lambda x: (x[2], x[0])), sorted(odstranjeneOvire, key=lambda x: (x[2], x[0]))) #vrnemo sortirano po vrsticah in stolpcih

class Test(unittest.TestCase):
    def test_dolzina_ovir(self):
        self.assertEqual(3, dolzina_ovir("...###..."))
        self.assertEqual(1, dolzina_ovir("...#..."))
        self.assertEqual(2, dolzina_ovir("...#..#."))
        self.assertEqual(7, dolzina_ovir("#...#####..#."))
        self.assertEqual(8, dolzina_ovir("...#####.##...#"))
        self.assertEqual(9, dolzina_ovir("#...#####.##...#"))
        self.assertEqual(6, dolzina_ovir("##...#.#...##"))
        self.assertEqual(0, dolzina_ovir("..."))
        self.assertEqual(0, dolzina_ovir("."))

    def test_stevilo_ovir(self):
        self.assertEqual(1, stevilo_ovir("...###..."))
        self.assertEqual(1, stevilo_ovir("...#..."))
        self.assertEqual(2, stevilo_ovir("...#..#."))
        self.assertEqual(3, stevilo_ovir("#...#####..#."))
        self.assertEqual(3, stevilo_ovir("...#####.##...#"))
        self.assertEqual(4, stevilo_ovir("#...#####.##...#"))
        self.assertEqual(4, stevilo_ovir("##...#.#...##"))
        self.assertEqual(0, stevilo_ovir("..."))
        self.assertEqual(0, stevilo_ovir("."))

    def test_najsirsa_ovira(self):
        self.assertEqual(3, najsirsa_ovira("...###..."))
        self.assertEqual(1, najsirsa_ovira("...#..."))
        self.assertEqual(1, najsirsa_ovira("...#..#."))
        self.assertEqual(5, najsirsa_ovira("#...#####..#."))
        self.assertEqual(5, najsirsa_ovira("...#####.##...#"))
        self.assertEqual(5, najsirsa_ovira("#...#####.##...#"))
        self.assertEqual(6, najsirsa_ovira("######...#####.##...#"))
        self.assertEqual(6, najsirsa_ovira("...#####.##...######"))

    def test_pretvori_vrstico(self):
        self.assertEqual([(3, 5)], pretvori_vrstico("..###."))
        self.assertEqual([(3, 5), (7, 7)], pretvori_vrstico("..###.#."))
        self.assertEqual([(1, 2), (5, 7), (9, 9)], pretvori_vrstico("##..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#"))
        self.assertEqual([], pretvori_vrstico("..."))
        self.assertEqual([], pretvori_vrstico(".."))
        self.assertEqual([], pretvori_vrstico("."))

    def test_pretvori_zemljevid(self):
        zemljevid = [
            "......",
            "..##..",
            ".##.#.",
            "...###",
            "###.##",
        ]
        self.assertEqual([(3, 4, 2), (2, 3, 3), (5, 5, 3), (4, 6, 4), (1, 3, 5), (5, 6, 5)], pretvori_zemljevid(zemljevid))

        zemljevid = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]
        self.assertEqual([(15, 16, 1),
                          (3, 5, 2), (11, 13, 2), (18, 19, 2),
                          (4, 6, 3), (10, 12, 3), (16, 16, 3),
                          (12, 12, 4), (18, 19, 4),
                          (1, 3, 6), (9, 13, 6), (17, 19, 6)], pretvori_zemljevid(zemljevid))

    def test_izboljsave(self):
        prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

        potem = [
            "...##.........##...",
            "..###.....###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....#####...###"
        ]

        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5)], izboljsave(prej, potem))

        self.assertEqual([], izboljsave(prej, prej))

    def test_huligani(self):
        prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

        potem = [
            "...##..............",
            "..........###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....##.##...###"
        ]

        dodane, odstranjene = huligani(prej, potem)
        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5), (9, 10, 6), (12, 13, 6)], dodane, "Napaka v seznamu dodanih")
        self.assertEqual([(15, 16, 1), (3, 5, 2), (9, 13, 6)], odstranjene, "Napaka v seznamu odstranjenih")

        dodane, odstranjene = huligani(potem, prej)  # Pazi, obrnjeno!
        self.assertEqual([(15, 16, 1), (3, 5, 2), (9, 13, 6)], dodane, "Napaka v seznamu dodanih")
        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5), (9, 10, 6), (12, 13, 6)], odstranjene, "Napaka v seznamu odstranjenih")

        self.assertEqual(([], []), huligani(prej, prej))


if __name__ == "__main__":
    unittest.main()
