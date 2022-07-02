import math


class Fraction:

    def __init__(self,numerator,denominator):
        if not all((numerator,denominator))>0:
            raise ZeroDivisionError
        if  type(numerator)!=int or type(denominator)!=int:
            raise ValueError
        self.numerator = numerator
        self.denominator = denominator

    def __gt__(self, other):
        return  self.numerator / self.denominator > other.numerator / other.denominator

    def __add__(self, other):
        new_numerator=self.numerator*other.denominator + other.numerator*self.denominator
        new_detorminator=self.denominator*other.denominator
        gcd=math.gcd(new_numerator,new_detorminator)
        return Fraction(new_numerator // gcd, new_detorminator // gcd)

    def __iadd__(self, other):
        new_numerator = self.numerator*other.denominator+other.numerator*self.denominator
        new_detorminator = self.denominator*other.denominator
        gcd = math.gcd(new_numerator,new_detorminator)
        return Fraction(new_numerator // gcd, new_detorminator // gcd)

    def __mul__(self, other):
        new_numerator = self.numerator*other.numerator
        new_detorminator = self.denominator*other.denominator
        gcd = math.gcd(new_numerator,new_detorminator)
        return Fraction(new_numerator // gcd, new_detorminator // gcd)

    def __imul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_detorminator = self.denominator * other.denominator
        gcd = math.gcd(new_numerator, new_detorminator)
        return Fraction(new_numerator // gcd, new_detorminator // gcd)

    def __sub__(self, other):
        new_numerator = self.numerator*other.denominator-other.numerator*self.denominator
        new_detorminator = self.denominator * other.denominator
        gcd = math.gcd(new_numerator, new_detorminator)
        return Fraction(new_numerator//gcd,new_detorminator//gcd)

    def __isub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_detorminator = self.denominator * other.denominator
        gcd = math.gcd(new_numerator, new_detorminator)
        return Fraction(new_numerator // gcd, new_detorminator // gcd)

    def __eq__(self, other):
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


first = Fraction(2,4)
second = Fraction(6,2)
third = first+second
fourth = Fraction(9,3)
fifth = Fraction(21,27)
sixth = first * fourth
seventh= first-fifth-second
second *= 2
print(third,second,sixth,seventh)