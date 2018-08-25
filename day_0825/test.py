# -*- coding: utf-8 -*-
# @Time    : 2018/8/25/025 16:34
# @Author  : LeiWenXuan
# @Email   : 892028617@qq.com
# @File    : test.py
# @Software: PyCharm
class Rectangle:
    def area(self):
        return self.length * self.wight
r = Rectangle()
r.length, r.wight = 13, 8
print(r.area())

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()
class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)
class AceCard(Card):
    def _points(self):
        return 1, 11
class FaceCard(Card):
    def _points(self):
        return 10, 10
cards = [AceCard('A', '❤'), NumberCard('2', '❤'), NumberCard('3','❤')]

class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
Club, Diamond, Heart, Speade = Suit('Club','♣'),Suit('Diamod','♦'),Suit('Heart','❤'), Suit('Spade','♠')

cards = [AceCard('A', Speade), NumberCard('2', Speade), NumberCard('3', Speade)]

def card(rank, suit):
    if rank == 1: return AceCard('A', suit)
    elif 2 <= rank < 11:return NumberCard(str(rank), suit)
    elif 11<= rank<14:
        name = {11:'J', 12:'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception('Rank out of range')

def card2(rank, suit):
    if rank == 1:return AceCard('A', suit)
    elif 2 <= rank < 11: return NumberCard(str(rank), suit)
    else:
        name = {11:'J', 12:'Q', 13:'K'}
        return FaceCard(name, suit)

def card3( rank, suit):
    if rank == 1: return AceCard( 'A', suit)
    elif 2 <= rank < 11: return NumberCard(str(rank), suit)
    elif rank == 11:
        return FaceCard('J', suit)
    elif rank == 12:
        return FaceCard('Q', suit)
    elif rank == 13:
        return FaceCard( 'K', suit)
    else:
        raise Exception('Rank out of range')

def card4( rank, suit):
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard, 13:FaceCard}.get(rank, NumberCard)
    return class_(rank, suit)



deck = [card(rank, suit)\
        for rank in range(1, 14)\
            for suit in (Club, Diamond, Heart, Speade) ]
deck2 = [card2(rank, suit)\
        for rank in range(13)\
            for suit in (Club, Diamond, Heart, Speade) ]
print(deck[1])





