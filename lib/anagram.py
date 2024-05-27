class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, words):
        return [word for word in words if self.is_anagram(word)]
    
    def is_anagram(self, word):
        return word.lower() != self.word.lower() and sorted(word.lower()) == sorted(self.word.lower())