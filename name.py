greeting_message = "Greetings and welcome to my program"
class Ephesians:
    def __init__(self, book = "Ephesians", chapter = range(1, 7), verse = range(1, 34)):
        self.book = book
        self.chapter = chapter
        self.verse = verse
    def __repr__(self):
        return self.book

ephesians = Ephesians()





