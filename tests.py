import unittest
from main import *


class TestRK2(unittest.TestCase):
    # Компьютеры
    computers = [
        Computer(1, 'Enigma'),
        Computer(2, 'Macintosh'),
        Computer(3, 'Agat'),
        Computer(4, 'Macintosh'),
        Computer(11, 'Asus'),
        Computer(22, 'Lenovo'),
        Computer(33, 'Apple'),
        Computer(44, 'AMD'),
    ]

    # Микропроцессоры
    browsers = [
        Browser(1, 'Chrome', 12300, 1),
        Browser(2, 'Opera', 34500, 2),
        Browser(3, 'Safari', 56400, 3),
        Browser(4, 'Yandex', 64400, 3),
        Browser(5, 'OperaGX', 75600, 4),
    ]
    browsers_computers = [
        BrowComp(1, 1), BrowComp(2, 2), BrowComp(3, 3), BrowComp(3, 4), BrowComp(4, 5),
        BrowComp(11, 1), BrowComp(22, 2), BrowComp(33, 3), BrowComp(33, 4), BrowComp(44, 5),
    ]

    def test_A1(self):
        o_to_m = [(brw.name, brw.size, cmp.name)
                  for cmp in computers
                  for brw in browsers
                  if brw.comp_id == cmp.id]
        self.assertEqual(n1_sol(o_to_m),
                         ('Agat', 56400, 'Agat'))

    def test_A2(self):
        o_to_m = [(brw.name, brw.size, cmp.name)
                  for cmp in computers
                  for brw in browsers
                  if brw.comp_id == cmp.id]
        self.assertEqual(n2_sol(o_to_m),
                         [('Enigma', 12300)])

    def test_A3(self):
        m_to_m_tmp = [(cmp.name, brwcmp.comp_id, brwcmp.brow_id)
                      for cmp in computers
                      for brwcmp in browsers_computers
                      if cmp.id == brwcmp.comp_id]

        m_to_m = [(brw.name, brw.size, tmp_name)
                  for tmp_name, tmp_id, emp_id in m_to_m_tmp
                  for brw in browsers if brw.id == emp_id]
        self.assertEqual(n3_sol(m_to_m),
                         [('Chrome', 12300, 'Enigma'),
                          ('Chrome', 12300, 'Asus'), ('Opera', 34500, 'Macintosh'), ('Opera', 34500, 'Lenovo'),
                          ('OperaGX', 75600, 'Macintosh'), ('OperaGX', 75600, 'AMD'), ('Safari', 56400, 'Agat'),
                          ('Safari', 56400, 'Apple'), ('Yandex', 64400, 'Agat'), ('Yandex', 64400, 'Apple')])


if __name__ == '__main__':
    unittest.main()