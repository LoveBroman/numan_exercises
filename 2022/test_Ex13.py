import Ex13
import unittest

class test_Ex13(unittest.TestCase):
    def test_crazy_plus(self):
        super().assertEqual(Ex13.crazu_plus(6, 4), 210, 'Korrekt svar ges ej')
        super().assertEqual(Ex13.crazu_plus(5, 4), 19, 'Korrekt svar ges ej')
        super().assertEqual(Ex13.crazu_plus(6, -4), 102, 'Korrekt svar ges ej')
        super().assertEqual(Ex13.crazu_plus(0, -0), 0, 'Korrekt svar ges ej')

        super().assertRaises(ValueError, Ex13.crazu_plus, 'jo', 'nej')
        super().assertRaises(ValueError, Ex13.crazu_plus, '4', '2')
        super().assertRaises(ValueError, Ex13.crazu_plus, 3, 'nej')
        super().assertRaises(ValueError, Ex13.crazu_plus, '3', 5)

