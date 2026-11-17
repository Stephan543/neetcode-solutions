class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(curr, i):
            if i == len(word):
                return curr.is_end

            if word[i] == ".":
                for child in curr.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            
            if word[i] not in curr.children:
                return False
            
            return dfs(curr.children[word[i]], i+1)
        
        return dfs(self.root, 0)
            