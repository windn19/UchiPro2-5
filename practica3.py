import math


class Fraction:
    num = 2
    den = 2

    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    @staticmethod
    def get_reduced_fraction(num, den):
        """Принимает числитель и знаменатель дроби,
        и возвращает кортеж: числитель и знаменатель сокращенной дроби."""
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        """Принимает знаменатель первой и знаменатель второй дроби и
        возвращает общий знаменатель."""
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den

    def __call__(self, a, b):
        return Fraction(a, b)

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'


num, den = map(int, input().split())
fraction = Fraction(num, den)
new_fraction = fraction(3, 4)
print(new_fraction)
print(fraction)
