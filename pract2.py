import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduce_fraction(num, den)

    @staticmethod
    def get_reduce_fraction(num, den):
        d = math.gcd(num, den)
        return num // d, den // d

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den

    def __ne__(self, other):
        return self.num * other.den != other.num * self.den

    def __ge__(self, other):
        return self.num * other.den >= other.num * self.den

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __le__(self, other):
        return self.num * other.den <= other.num * self.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den


# num, den = map(int, input().split())
fraction1 = Fraction(1, 2)
# num, den = map(int, input().split())
fraction2 = Fraction(2, 3)
print(fraction1 == fraction2)
print(fraction1 != fraction2)
print(fraction1 > fraction2)
print(fraction1 >= fraction2)
print(fraction1 < fraction2)
print(fraction1 <= fraction2)