import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    # 특별 메소드가 없다면, len(deck)을 이용할 수 없다.
    # 파이썬 데이터 모텔을 사용했을 때의 장점은 두가지 장점
     # 1.표준연산을 사용하기위해, 정의된 임의 메소드명을 암기할 필요없음.
     # 2. 표준라이브러리에서 제공하는 풍부한 기능 구현할 필요 없이 사용 가능 random.choice()

    def __len__(self):
        return len(self._cards)

    # 여기서 배열화를 하기 때문에 밑에서 indexing이 가능하다.
    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
Card('Q', 'hearts') in deck


# 정렬 하는 법, 숫자 (rank)로 순위를 정하고 (A가 가장 큼) 그림은 스페이드, 하트, 다이아몬드, 클로버
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# for card in sorted(deck, key=spades_high, reverse=True):
#     print(card)
for card in reversed(deck):
    print(card)
