# Task-1-Spelling-Checker-Algorithm
The SpellChecker project is a Python-based spell-checking utility that allows users to verify the correctness of words against a given dictionary and provides suggestions for similar words if a given word is misspelled or not found in the dictionary.
## Usage Guide:
1) Initializing SpellChecker: Create an instance of the SpellChecker class to use the spell-checking functionalities.

2) Reading a Dictionary: Load a dictionary from a file using the 'read_dictionary(file_path)' method. The file should contain words separated by spaces, and the dictionary will be sorted for efficient spell checking.

3) Spell Checking: Use the 'nearest_words(word)' method to check if a given word is present in the dictionary. If the word is not found, the method will suggest the nearest words that can help users identify potential corrections.

4) Adding New Words: Employ the 'add_word(word)' method to insert new words into the dictionary. The dictionary will be automatically sorted to maintain efficiency in spell checking.
