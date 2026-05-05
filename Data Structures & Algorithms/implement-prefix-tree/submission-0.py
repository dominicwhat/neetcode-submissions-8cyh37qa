class Node:
    def __init__(self):
        self.children = {}
        self.end = False 
class PrefixTree:

    def __init__(self):
        self.children = Node()

    def insert(self, word: str) -> None:
        pointer = self.children
        for w in word:
            if w not in pointer.children:
                pointer.children[w] = Node()
                pointer = pointer.children[w]
            else:
                pointer = pointer.children[w]
        pointer.end = True

    def search(self, word: str) -> bool:
        pointer = self.children
        for w in word:
            if w not in pointer.children:
                return False
            pointer = pointer.children[w]
        return pointer.end         

    def startsWith(self, prefix: str) -> bool:
        pointer = self.children
        for w in prefix:
            if w not in pointer.children:
                return False
            pointer = pointer.children[w]
        return True 
        