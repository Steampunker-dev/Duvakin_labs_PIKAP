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

    def test_A1(self):
        one_to_many = [(e.name, e.cores, d.model)
                       for d in computers
                       for e in browsers
                       if e.dep_id == d.id]
        self.assertEqual(n1_sol(one_to_many),
                         [('Pentium', 2, 'ASUS 2000'), ('Celeron', 1, 'ASUS 2000'), ('Core i3', 4, 'Honor 2020'),
                          ('Core i7', 2, 'Honor 2020'), ('M1', 8, 'MacBook Pro')])

    def test_A2(self):
        one_to_many = [(e.name, e.cores, d.model)
                       for d in computers
                       for e in browsers
                       if e.dep_id == d.id]
        self.assertEqual(n2_sol(one_to_many),
                         [('MacBook Pro', 8), ('Honor 2020', 6), ('ASUS 2000', 3)])

    def test_A3(self):
        many_to_many_temp = [(d.model, ed.dep_id, ed.emp_id)
                             for d in computers
                             for ed in emps_deps
                             if d.id == ed.dep_id]

        many_to_many = [(e.name, e.cores, dep_name)
                        for dep_name, dep_id, emp_id in many_to_many_temp
                        for e in browsers if e.id == emp_id]
        self.assertEqual(n3_sol(many_to_many),
                         {'MacBook Air': ['Pentium', 'Celeron', 'Core i3'], 'MacBook Pro': ['M1'],
                          'iMac 2013': ['Core i7']})


if __name__ == '__main__':
    unittest.main()