class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search_helper(self, node, word, index):
        if index == len(word):
            return node.isEndOfWord

        char = word[index]
        if char == '.':
            for child_node in node.children.values():
                if self.search_helper(child_node, word, index + 1):
                    return True
        else:
            if char not in node.children:
                return False
            return self.search_helper(node.children[char], word, index + 1)

    def search(self, word: str) -> bool:
        return self.search_helper(self.root, word, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)