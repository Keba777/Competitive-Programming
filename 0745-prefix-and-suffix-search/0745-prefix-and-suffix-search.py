class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        self.weight = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, weight):
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]
            node.weight = weight

    def startsWith(self, word):
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.children[i]:
                return -1
            node = node.children[i]
        return node.weight

class WordFilter:
    def __init__(self, words):
        self.trie = Trie()
        for weight, word in enumerate(words):
            for j in range(len(word) + 1):
                self.trie.insert(word[j:] + '{' + word, weight)

    def f(self, prefix, suffix):
        return self.trie.startsWith(suffix + '{' + prefix)

