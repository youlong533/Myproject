#  _*_ coding:utf-8 _*_

class Faction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        comon = Faction.gcd(newnum,newden)
        return Faction(newnum//comon , newden//comon)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        comon = Faction.gcd(newnum,newden)
        return Faction(newnum//comon , newden//comon)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        comon = Faction.gcd(newnum,newden)
        return Faction(newnum//comon , newden//comon)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        comon = Faction.gcd(newnum,newden)
        return Faction(newnum//comon , newden//comon)

    def __eq__(self, other):
        firstnum = self.num *other.den
        secondnum = other.num *self.den

        return firstnum ==secondnum


    def gcd(m,n):
        while m%n != 0:
            old_m = m
            old_n = n

            m = old_n
            n = old_m%old_n
        return n


if __name__ == '__main__':
    res = Faction.gcd(3,4)
    print(res)