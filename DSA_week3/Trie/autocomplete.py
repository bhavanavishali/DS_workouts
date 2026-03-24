class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
        
    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def collect_words(self, node, prefix, words):
        if node.end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            self.collect_words(child_node, prefix + char, words)
            
    def search(self, word):
        node = self.search_prefix(word)
        return node is not None and node.end_of_word
    
    def autocomplete(self, prefix):
        words = []
        prefix_node = self.search_prefix(prefix)
        if prefix_node:
            self.collect_words(prefix_node, prefix, words)
        return words
        
        
# Test
t = Trie()
a = ["apple", "orange", "app"]
for i in a:
    t.insert(i)

print(t.autocomplete("app"))  # ['app', 'apple']
print(t.search("app"))        # True
print(t.search("appl"))       # False
