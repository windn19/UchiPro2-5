import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'

    @staticmethod
    def get_reduced_fraction(num, den):
        """
        Принимает числитель и знаменатель дроби, и возвращает кортеж: числитель и знаменатель сокращенной дроби.
        """
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        """Принимает знаменатель первой и второй дроби, и возвращает общий знаменатель"""
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 9)
print(fraction1)
print(fraction2)
print(fraction1 + fraction2)
