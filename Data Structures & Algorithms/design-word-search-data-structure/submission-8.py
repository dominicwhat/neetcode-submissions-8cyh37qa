class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()
            cur = cur.children[w]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(word, cur):
            for idx, w in enumerate(word):
                if w not in cur.children and w != '.':
                    return False
                if w == '.':
                    for key in cur.children.keys():
                        end = dfs(word[idx+1:], cur.children[key])
                        if end:
                            return True
                    return False
                else:
                    cur = cur.children[w]
            return cur.end
        res = dfs(word,self.root)
        return res

