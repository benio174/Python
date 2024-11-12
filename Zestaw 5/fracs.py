
import math
import unittest


def add_frac(frac1, frac2):
    fracN = (frac1[0] * frac2[1]) + (frac2[0] * frac1[1])
    fracD = frac1[1] * frac2[1]
    gcd = math.gcd(fracN, fracD)
    fracN /= gcd
    fracD /= gcd
    return [int(fracN), int(fracD)]

def sub_frac(frac1, frac2):
    fracN = (frac1[0] * frac2[1]) - (frac2[0] * frac1[1])
    fracD = frac1[1] * frac2[1]
    gcd = math.gcd(fracN, fracD)
    fracN /= gcd
    fracD /= gcd
    return [int(fracN), int(fracD)]

def mul_frac(frac1, frac2):
    fracN = frac1[0] * frac2[0]
    fracD = frac1[1] * frac2[1]
    gcd = math.gcd(fracN, fracD)
    fracN /= gcd
    fracD /= gcd
    return [int(fracN) ,int(fracD)]

def div_frac(frac1, frac2):
    fracN = frac1[0] * frac2[1]
    fracD = frac1[1] * frac2[0]
    gcd = math.gcd(fracN, fracD)
    fracN /= gcd
    fracD /= gcd
    if fracN < 0 and fracD < 0:
        return [abs(int(fracN)), abs(int(fracD))]
    return [int(fracN) ,int(fracD)]

def is_positive(frac):
    if (frac[0] < 0 < frac[1]) or (frac[1] < 0 < frac[0]):
        return False
    else:
        return True

def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):
    top1, bottom1 = frac1[0], frac1[1]
    top2, bottom2 = frac2[0], frac2[1]

    top1 *= bottom2
    top2 *= bottom1
    if top1 < top2:
        return -1
    elif top1 == top2:
        return 0
    else:
        return 1

def frac2float(frac):
    return frac[0] / frac[1]


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 4], [1, 4]), [1, 2])
        self.assertEqual(add_frac([1, 2], [-1, 3]), [1, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1,2], [1,3]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [-1, 3]), [5, 6])
        self.assertEqual(sub_frac([3, 4], [1, 4]), [1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([1, 2], [-1, 3]), [-1, 6])
        self.assertEqual(mul_frac([-1, 2], [-1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([1, 2], [-1, 3]), [3, -2])
        self.assertEqual(div_frac([-1, 2], [-1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([1, -2]), False)
        self.assertEqual(is_positive([-1, -2]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 3]), True)
        self.assertEqual(is_zero([1, 3]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([-3, 4]), -0.75)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
