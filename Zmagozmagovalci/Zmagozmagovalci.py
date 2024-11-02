def rek(kolesar1, kolesar2, razmerja):
    if kolesar1 == kolesar2:
        return True
    for kolesar in razmerja[kolesar1]:
        return rek(kolesar, kolesar2, razmerja)
    return False

def hitrejsi(kolesar1, kolesar2, razmerja):
    if rek(kolesar1, kolesar2, razmerja):
        return kolesar1
    elif rek(kolesar2, kolesar1, razmerja):
        return kolesar2
    return None


from itertools import pairwise
import unittest


razmerja = {'Ana': {'Vera', 'Cilka'},
            'Berta': {'Greta', 'Klara', 'Iva', 'Cilka'},
            'Cilka': {'Olga'},
            'Črtomira': set(),
            'Dani': {'Liza', 'Ana', 'Fanči', 'Cilka', 'Micka', 'Greta'},
            'Ema': set(),
            'Fanči': {'Liza', 'Poldka', 'Cilka'},
            'Greta': set(),
            'Helga': set(),
            'Iva': {'Ema', 'Helga'},
            'Jana': {'Liza', 'Dani', 'Berta', 'Micka', 'Tina', 'Greta'},
            'Klara': {'Helga', 'Nina'},
            'Liza': {'Vera', 'Olga', 'Rezka'},
            'Micka': {'Liza', 'Saša', 'Urša'},
            'Nina': {'Olga', 'Poldka'},
            'Olga': {'Poldka'},
            'Poldka': set(),
            'Rezka': {'Saša'},
            'Saša': set(),
            'Špela': {'Žana'},
            'Tina': set(),
            'Urša': {'Vera'},
            'Vera': set(),
            'Zoja': {'Žana', 'Tina'},
            'Žana': set()}


razmerja2 = {x: {y} for x, y in pairwise(sorted(razmerja))}
razmerja2.update({"Žana": set(), "Trelawney": set()})


class Test(unittest.TestCase):
    def test_01_obvezna(self):
        self.assertEqual("Jana", hitrejsi("Jana", "Berta", razmerja))
        self.assertEqual("Jana", hitrejsi("Berta", "Jana", razmerja))
        self.assertEqual("Berta", hitrejsi("Berta", "Poldka", razmerja))
        self.assertEqual("Berta", hitrejsi("Poldka", "Berta", razmerja))
        self.assertEqual("Berta", hitrejsi("Poldka", "Berta", razmerja))
        self.assertIsNone(hitrejsi("Saša", "Berta", razmerja))
        self.assertIsNone(hitrejsi("Berta", "Saša", razmerja))
        self.assertIsNone(hitrejsi("Špela", "Tina", razmerja))
        self.assertIsNone(hitrejsi("Jana", "Črtomira", razmerja))
        self.assertIsNone(hitrejsi("Črtomira", "Jana", razmerja))

        self.assertEqual("Ana", hitrejsi("Ana", "Žana", razmerja2))
        self.assertEqual("Ana", hitrejsi("Žana", "Ana", razmerja2))
        self.assertIsNone(hitrejsi("Ana", "Trelawney", razmerja2))
        self.assertIsNone(hitrejsi("Ana", "Trelawney", razmerja2))

    def test_02_dokazov(self):
        self.assertEqual(1, dokazov("Jana", "Berta", razmerja))
        self.assertEqual(0, dokazov("Berta", "Jana", razmerja))
        self.assertEqual(4, dokazov("Jana", "Cilka", razmerja))
        self.assertEqual(1, dokazov("Jana", "Nina", razmerja))
        self.assertEqual(5, dokazov("Jana", "Liza", razmerja))
        self.assertEqual(10, dokazov("Jana", "Olga", razmerja))
        self.assertEqual(12, dokazov("Jana", "Poldka", razmerja))
        self.assertEqual(1, dokazov("Špela", "Žana", razmerja))

        self.assertEqual(1, dokazov("Ana", "Žana", razmerja2))
        self.assertEqual(0, dokazov("Žana", "Ana", razmerja2))


if __name__ == "__main__":
    unittest.main()
