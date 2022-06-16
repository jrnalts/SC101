class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.ds = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.ds
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                cur.children[ch] = TrieNode()
                cur = cur.children[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.ds
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return False
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.ds
        for ch in prefix:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return False
        return True


def main():
    word = 'apple'
    obj = Trie()
    obj.insert(word)
    obj.search(word)


if __name__ == '__main__':
	main()