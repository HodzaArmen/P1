A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

zemljevid = {
    (A, B): "gravel trava",
    (A, V): "pešci lonci",
    (B, C): "bolt lonci",
    (B, V): "",
    (C, R): "stopnice pešci lonci",
    (D, F): "stopnice pešci",
    (D, R): "pešci",
    (E, I): "trava lonci",
    (F, G): "trava črepinje",
    (G, H): "črepinje pešci",
    (G, I): "avtocesta",
    (H, J): "robnik bolt",
    (I, M): "avtocesta",
    (I, P): "gravel",
    (I, R): "stopnice robnik",
    (J, K): "",
    (J, L): "gravel bolt",
    (K, M): "stopnice bolt",
    (L, M): "robnik pešci",
    (M, N): "rodeo",
    (N, P): "gravel",
    (O, P): "gravel",
    (P, S): "",
    (R, U): "trava pešci",
    (R, V): "pešci lonci",
    (S, T): "robnik trava",
    (T, U): "gravel trava",
    (U, V): "robnik lonci trava"
}

mali_zemljevid = {(A, B): "robnik bolt",
                  (A, C): "bolt rodeo pešci",
                  (C, D): ""}

def dvosmerni_zemljevid(zemljevid):
    novZemljevid = {}
    for pot, vescina in zemljevid.items():
        novZemljevid[pot] = set(vescina.split())
        novZemljevid[pot[::-1]] = set(vescina.split())  #obrnemo črki
    return novZemljevid


def mozna_pot(pot, zemljevid):
    if len(pot) == 1:
        for i, j in zemljevid.items():
            if pot[0] == i[0] or pot[0] == i[1]:
                return True
        return False
    for i in range(len(pot) - 1):
        trenutno_krizisce = pot[i]
        naslednje_krizisce = pot[i + 1]
        if (trenutno_krizisce, naslednje_krizisce) not in zemljevid and (naslednje_krizisce, trenutno_krizisce) not in zemljevid:
            return False
    return True

def potrebne_vescine(pot, zemljevid):
    vescine = set()
    for i in range(len(pot) - 1):
        trenutno_krizisce = pot[i]
        naslednje_krizisce = pot[i + 1]
        for x, y in zemljevid.items():
            if (trenutno_krizisce, naslednje_krizisce) == x or (naslednje_krizisce, trenutno_krizisce) == x:
                vescine.update(y.split())
    return vescine

def nepotrebne_vescine(pot, zemljevid, vescine):
    potrebneVescine = potrebne_vescine(pot, zemljevid)
    nepotrebneVescine = set()
    for x in vescine:
        if x not in potrebneVescine:
            nepotrebneVescine.add(x)
    return nepotrebneVescine

def tocke_vescine(zemljevid, vescina):
    pot = set()
    for x, y in zemljevid.items():
        a = y.split()
        for b in a:
            if vescina == b:
                pot.update(x[0])
                pot.update(x[1])
    return ''.join(sorted(pot))

def koncna_tocka(pot, zemljevid, vescine):
    mnozica = set()
    zadnjaTocka = None
    zemljevid = dvosmerni_zemljevid(zemljevid)
    for i in range(len(pot)):
        c = (pot[i], pot[i + 1])
        if c in zemljevid:
            vescinePov = set(zemljevid[c])
            manjkajoce = vescinePov - vescine
            if manjkajoce:
                mnozica.update(manjkajoce)
                zadnjaTocka = pot[i]
                break
    return zadnjaTocka, mnozica

import unittest
import ast


class TestObvezna(unittest.TestCase):
    def test_1_dvosmerni_zemljevid(self):
        kopija = mali_zemljevid.copy()

        self.assertEqual({('A', 'B'): {'robnik', 'bolt'},
                          ('B', 'A'): {'robnik', 'bolt'},
                          ('A', 'C'): {'bolt', 'rodeo', 'pešci'},
                          ('C', 'A'): {'bolt', 'rodeo', 'pešci'},
                          ('C', 'D'): set(),
                          ('D', 'C'): set()},
                         dvosmerni_zemljevid(mali_zemljevid))
        self.assertEqual(mali_zemljevid, kopija, "Ne spreminjaj zemljevida, temveč sestavi novega!")

    def test_2_mozna_pot(self):
        self.assertTrue(mozna_pot("ACD", mali_zemljevid))
        self.assertTrue(mozna_pot("ABACD", mali_zemljevid))
        self.assertTrue(mozna_pot("AB", mali_zemljevid))
        self.assertFalse(mozna_pot("ABD", mali_zemljevid))

        self.assertTrue(mozna_pot("ABCRVRIEIPNM", zemljevid))
        self.assertTrue(mozna_pot("HJKMLJH", zemljevid))
        self.assertFalse(mozna_pot("AC", zemljevid))
        self.assertFalse(mozna_pot("ABCRVRIEPNM", zemljevid))
        self.assertTrue(mozna_pot("A", zemljevid))

    def test_3_potrebne_vescine(self):
        self.assertEqual({'pešci', 'bolt', 'rodeo'},
                         potrebne_vescine("AC", mali_zemljevid))

        self.assertEqual({'pešci', 'bolt', 'rodeo'},
                         potrebne_vescine("ACD", mali_zemljevid))

        self.assertEqual({'pešci', 'robnik', 'bolt', 'rodeo'},
                         potrebne_vescine("ABACD", mali_zemljevid))

        self.assertEqual({'robnik', 'stopnice', 'gravel', 'trava'},
                          potrebne_vescine("RIPSTUT", zemljevid))

        self.assertEqual({'pešci', 'trava', 'lonci', 'bolt', 'stopnice', 'gravel'},
                         potrebne_vescine("ABCRVR", zemljevid))

        self.assertEqual({'pešci', 'trava', 'robnik', 'lonci', 'bolt', 'stopnice', 'rodeo', 'gravel'},
                         potrebne_vescine("ABCRVRIEIPNM", zemljevid))

        self.assertEqual({'pešci', 'robnik', 'bolt', 'stopnice', 'gravel'},
                         potrebne_vescine("HJKMLJH", zemljevid))

        self.assertEqual(set(), potrebne_vescine("BVBVBVB", zemljevid))

    def test_4_nepotrebne_vescine(self):
        vescine = {'pešci', 'robnik', 'stopnice', 'gravel', 'bolt', 'rodeo'}
        kopija = vescine.copy()
        self.assertEqual({'stopnice', 'gravel'},
                         nepotrebne_vescine("ABACD", mali_zemljevid, vescine))
        self.assertEqual(vescine, kopija, "Se mi prav zdi, da je funkcija nepotrebne_vescine spremenila "
                                          "vrednost svojega argumenta `vescine`? Fail, fail!")

        vescine = {'stopnice', 'gravel', 'bolt', 'rodeo'}
        self.assertEqual({'stopnice', 'bolt'},
                         nepotrebne_vescine("IPNMNPO", zemljevid, vescine))

        vescine = {'gravel', 'rodeo'}
        self.assertEqual(set(), nepotrebne_vescine("IPNMNPO", zemljevid, vescine))

    def test_5_tocke_vescine(self):
        self.assertEqual("GIM", tocke_vescine(zemljevid, "avtocesta"))
        self.assertEqual("HIJLMRSTUV", tocke_vescine(zemljevid, "robnik"))
        self.assertEqual("MN", tocke_vescine(zemljevid, "rodeo"))
        self.assertEqual("ABIJLNOPTU", tocke_vescine(zemljevid, "gravel"))



class TestDodatna(unittest.TestCase):
    def test_1_koncna_tocka(self):
        vescine = {'pešci', 'robnik', 'bolt', 'stopnice', 'gravel'}
        self.assertEqual(("H", {'črepinje'}), koncna_tocka("HJKMLJHGFD", zemljevid, vescine))
        self.assertEqual(("M", {'rodeo'}), koncna_tocka("HJKMNPIG", zemljevid, vescine))
        self.assertEqual(("B", {'lonci', 'bolt'}), koncna_tocka("ABCRVB", zemljevid, {"gravel", "trava"}))


if "__main__" == __name__:
    unittest.main()
