from collections import deque
from ExceptionHandler.CustomException import DeckIsEmptyException

import random
import constant
import unittest

class Card:
    def __init__(self, value, symbol):
        self.symbol = symbol
        self.value = value
    
    def printCard(self):
        print(f'{self.value} of {self.symbol}')

class Deck:
    def __init__(self):
        self.cards = deque()
        self.buildDeck()
    
    def buildDeck(self):
        for symbol in constant.SYMBOLS:
            for number in range(1, constant.NO_CARDS_PER_SYMBOL + 1):
                card = Card(symbol, number)
                self.cards.append(card)
        
    def showDeck(self):
        for card in self.cards:
            card.printCard()
    
    def countDeck(self):
        return len(self.cards)

    def shuffleDeck(self):
        shuffled_cards = []
        for i in range(len(self.cards)):
            random_index = 0
            while True:
                random_index = random.randint(0, len(self.cards) - 1)
                if random_index not in shuffled_cards:
                    shuffled_cards.append(random_index)
                    break
            self.cards[i], self.cards[random_index] = self.cards[random_index], self.cards[i]
    
    def drawCard(self):
        if(len(self.cards) < 1):
            raise DeckIsEmptyException()
        return self.cards.pop()


