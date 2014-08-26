import unittest

# Return the greatest common divisor of two numbers:
def gcd(m, n):
    if m % n == 0:
        return n

    return gcd(n, m % n)


class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEquals(gcd(24, 36), 12)
        self.assertEquals(gcd(36, 24), 12)
        self.assertEquals(gcd(36, 144), 36)
        self.assertEquals(gcd(121, 2530), 11)
        self.assertEquals(gcd(2530, 121), 11)
        self.assertEquals(gcd(2530, 242), 22)
        self.assertEquals(gcd(242, 2530), 22)

