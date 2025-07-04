class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        current=self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TrieNode()
            current=current.children[char]
        current.is_end=True
    
    def search(self,word):
        current=self.root
        for i in word:
            if i not in current.children:
                return False

            current=current.children[i]
        return current.is_end
    
    def starts_with(self,prefix):
        current=self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current=current.children[letter]
        return True
trie=Trie()
trie.insert("cat")
trie.insert("cap")
trie.insert("car")
trie.insert("carnival")
print(trie.search("cat"))
print(trie.search("can"))
print(trie.starts_with("ca"))
print(trie.starts_with('dup'))