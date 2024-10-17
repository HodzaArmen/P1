def koordinate(s):
    a = s.split("-")
    start = int(a[0])
    konec = start - 1
    for i in s:
        if i == "-":
            konec = konec + 1
    return (start, konec)

def vrstica(s):
    ovire = []
    zacetek = s.find('(')
    konec = s.find(')')
    y = int(s[zacetek+1:konec]) #kar je v oklepajih
    a = s.split()
    for ovira in a[1:]: #naprej od oklepaja
        b = koordinate(ovira)
        terka = (*b, y) #razpakiranje terke b in dodajanje vrednosti y
        ovire.append(terka)
    return ovire

def preberi(s):
    s = s.splitlines()
    ovire = []
    for i in s:
        ovire = ovire + vrstica(i)
    return ovire

def intervali(xs):
    rezultati = []
    for x0, x1 in xs:
        interval = '-' * (x1 - x0 + 1)
        rezultati.append(str(x0) + interval)
    return rezultati

def zapisi_vrstico(y, xs):
    zapisi = intervali(xs)
    rezultat = "(" + str(y) + ")"
    for zapis in zapisi:
        rezultat += ' ' + zapis
    return rezultat

import unittest


class Obvezna(unittest.TestCase):
    def test_koordinate(self):
        self.assertEqual((3, 4), koordinate("3--"))
        self.assertEqual((5, 10), koordinate("5------"))
        self.assertEqual((123, 123), koordinate("123-"))
        self.assertEqual((123, 125), koordinate("123---"))

    def test_vrstica(self):
        self.assertEqual([(1, 3, 4), (5, 11, 4), (15, 15, 4)], vrstica("  (4) 1---  5------- 15-"))
        self.assertEqual([(989, 991, 1234)], vrstica("(1234) 989---"))

    def test_preberi(self):
        self.assertEqual([(5, 6, 4),
                          (90, 100, 13), (5, 8, 13), (19, 21, 13),
                          (9, 11, 5), (19, 20, 5), (30, 34, 5),
                          (9, 11, 4),
                          (22, 25, 13), (17, 19, 13)], preberi(
""" (4) 5--
(13) 90-----------   5---- 19---
 (5) 9---           19--   30-----
(4)           9---
(13)         22---- 17---
"""))

    def test_intervali(self):
        self.assertEqual(["6-----", "12-", "20---", "98-----"], intervali([(6, 10), (12, 12), (20, 22), (98, 102)]))

    def test_zapisi_vrstico(self):
        self.assertEqual("(5) 6----- 12-", zapisi_vrstico(5, [(6, 10), (12, 12)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))


class Dodatna(unittest.TestCase):
    def test_zapisi(self):
        ovire = [(5, 6, 4),
          (90, 100, 13), (5, 8, 13), (9, 11, 13),
          (9, 11, 5), (19, 20, 5), (30, 34, 5),
          (9, 11, 4),
          (22, 25, 13), (17, 19, 13)]
        kopija_ovir = ovire.copy()
        self.assertEqual("""(4) 5-- 9---
(5) 9--- 19-- 30-----
(13) 5---- 9--- 17--- 22---- 90-----------""", zapisi(ovire).rstrip("\n"))
        self.assertEqual(ovire, kopija_ovir, "Pusti seznam `ovire` pri miru")


if __name__ == "__main__":
    unittest.main()