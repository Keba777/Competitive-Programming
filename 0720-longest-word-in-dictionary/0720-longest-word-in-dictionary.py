class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

class Solution:
    def longestWord(self, words):
        trie = Trie()

        # Insert all words into the trie
        for word in words:
            trie.insert(word)

        longest_word = ""

        def dfs(node, path):
            nonlocal longest_word
            if len(path) > len(longest_word) or (len(path) == len(longest_word) and path < longest_word):
                longest_word = path

            for char, child_node in node.children.items():
                if child_node.is_end:
                    dfs(child_node, path + char)

        dfs(trie.root, "")
        return longest_word
