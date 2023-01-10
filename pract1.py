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


num, den = map(int, input().split())
one = Fraction(num, den)
num, den = map(int, input().split())
two = Fraction(num, den)
print(one)
print(two)
print(one + two)
print(one - two)
print(one * two)
print(one / two)

