"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a
dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
void erase(String word) Erases the string word from the trie.

"""

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.words_ending_here = 0
        self.words_starting_here = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            char_index = ord(w) - ord('a')
            if not node.links[char_index]:
                node.links[char_index] = TrieNode()
            node = node.links[char_index]
            node.words_starting_here += 1
        node.words_ending_here += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for w in word:
            char_index = ord(w) - ord('a')
            if not node.links[char_index]:
                return 0
            node = node.links[char_index]
        return node.words_ending_here

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for w in prefix:
            char_index = ord(w) - ord('a')
            if not node.links[char_index]:
                return 0
            node = node.links[char_index]
        return node.words_starting_here

    def erase(self, word: str) -> None:
        node = self.root
        for w in word:
            char_index = ord(w) - ord('a')
            node = node.links[char_index]
            node.words_starting_here -= 1
        node.words_ending_here -= 1