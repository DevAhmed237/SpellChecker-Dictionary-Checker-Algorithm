import bisect

class SpellChecker:
    def __init__(self):
        self.dictionary = []
    
    # Read the words from dictionry file and store them into a list.
    # Time Complexity: O(n) - Space Complexity: O(n)
    def read_dictionary(self, file_path):
        self.dictionary = open(file_path, encoding="latin-1").read().split()

    # Add a new word to the dictionary in the correct order using binary search.
    # Time Complexity: O(log n) - Space Complexity: O(1)
    def add_word(self, word):
        insertion_index = bisect.bisect_left(self.dictionary, word)
        if word not in self.dictionary:
            self.dictionary.insert(insertion_index, word)

    # Return the nearest 4 words to a given word.
    # Time Complexity: O(log n) - Space Complexity: O(1)
    def nearest_words(self, word):
        if word in self.dictionary:
            return [word]
        index = bisect.bisect_left(self.dictionary, word)
        if index == 0:
            return [] + self.dictionary[0:2]
        elif index == len(self.dictionary):
            return self.dictionary[-2:], []
        else:
            return self.dictionary[index - 2 : index] + self.dictionary[index : index + 2]
        

spell_checker = SpellChecker()
spell_checker.read_dictionary("dictionary.txt")
print(spell_checker.nearest_words("appel"))
spell_checker.add_word("appeel")
print(spell_checker.nearest_words("appel"))
