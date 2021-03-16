class Error(Exception):
    """ Base class for other exceptions """
    pass

class DeckIsEmptyException(Error):
    def __init__(self, message = "Deck is empty! Cannot draw any card."):
        self.message = message
        super().__init__(self.message)
