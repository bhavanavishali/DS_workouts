class TrieNode:
    def __init__(self):
        self.children={}
        self.end_of_word=False
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        node=self.root 
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.end_of_word=True

    def _search_prefix(self,prefix):
        node=self.root
        if node is not None:
            for char in prefix:
                if char not in node.children:
                    return None

                node=node.children[char]
            return node
    
    def _collect_words(self,node,prefix,word):
        if node.end_of_word:
            word.append(prefix)

        for char, child_node in node.children.items():
            self._collect_words(child_node,prefix+char,word)
    def search(self,word):
        node=self._search_prefix(word)
        return node is not None and node.end_of_word

    def autocomplete(self,prefix):
        words=[]
        prefix_node=self._search_prefix(prefix)
        if prefix_node:
            self._collect_words(prefix_node,prefix,words)
        return words
trie=Trie()
words=["apple","app","apt","bat","ball"]
for word in words:
    trie.insert(word)

print(trie.autocomplete("app")) 
print("serach",trie.search("applllll"))