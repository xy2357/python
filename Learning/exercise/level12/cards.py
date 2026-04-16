import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit} {self.rank}"

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ['diamond', 'spade', 'heart', 'club']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            print("没有牌了！")
            return
        card = self.cards.pop()
        print(f"你抽到了{card}")

    def show_count(self):
        print(f"还剩{len(self.cards)}牌")

deck = Deck()
deck.shuffle()
deck.draw_card()
deck.draw_card()
deck.draw_card()
deck.draw_card()
deck.draw_card()
deck.draw_card()
deck.draw_card()
deck.draw_card()
deck.show_count()
