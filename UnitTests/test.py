from ExceptionHandler.CustomException import DeckIsEmptyException

import main
import unittest
import constant

class DeckTest(unittest.TestCase):
    def test_deck(self):
        deck = main.Deck()
        counter = deck.countDeck()
        self.assertEqual(counter, constant.NO_CARDS_PER_SYMBOL * constant.NO_SYMBOLS, "Should be 52.")

    def test_shuffle_deck(self):
        deck = main.Deck()
        deck.shuffleDeck()
        self.assertIsInstance(deck, main.Deck, "Should be instance of Deck class.")
    
    def test_draw_card(self):
        deck = main.Deck()
        card = deck.drawCard()
        self.assertIsInstance(card, main.Card, "Should be instance of Card class.")
    
    def test_draw_card_until_empty(self):
        deck = main.Deck()
        for i in range(deck.countDeck()):
            deck.drawCard()
        self.assertEqual(deck.countDeck(), 0, "Length should be 0.")
    
    def test_draw_card_until_empty_with_error(self):
        deck = main.Deck()
        for i in range(deck.countDeck()):
            deck.drawCard()
        with self.assertRaises(DeckIsEmptyException):
            deck.drawCard()

if __name__ == '__main__':
    unittest.main()



