import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self,path):
        f = open(path)
        self.words = self.read(f)
        print(f"{len(self.words)} words in file")

    def read(self,f):
        """Reads through and returns all words within the file"""
        return [word.strip() for word in f]

    def random(self):
        """Returns a random word from the file"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def read(self,f):
        """Reads through the file and doesn't read commented out words or whitespace"""
        return [word.strip() for word in f if word.strip() and not word.startswith('#')]