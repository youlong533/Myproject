# _*_ conding:utf-8 _*_
import random


class Poker:

    def __init__(self):
        self.col = ['方块', '梅花', '红桃', '黑桃']

    def color(self):
        return self.col

    def number(self,n):
        num = list(range(2,11))
        num.extend(n)
        return list(num)

    def poker(self):
        num = 'JQKA'
        n1 = "".join('%s' % id for id in p.number(num))
        Poker = random.choice(self.col) + random.choice(n1)
        print(Poker)

    def pokers(self,col,num):
        pokers = [c+str(n) for c in col for n in num]
        pokers.append('joker')
        pokers.append('JOKER')
        return pokers

if __name__ == '__main__':
    num = 'JQKA'
    p = Poker()
    # n1 = "".join('%s' %id for id in p.number(num))
    # Poker = random.choice(p.color())+random.choice(n1)
    # print(Poker)
    # Pokers = p.pokers(p.color(),p.number(num))
    # print(Pokers)
    p.poker()
    print(p.pokers(p.color(),p.number(num)))

