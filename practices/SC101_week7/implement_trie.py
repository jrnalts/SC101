class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.ds = {}

    def insert(self, word: str) -> None:
        key = word[0]
        if key in self.ds:
            self.ds[key].append(word)
        else:
            self.ds[key] = [word]

    def search(self, word: str) -> bool:
        key = word[0]
        if key not in self.ds:
            return False

        return word in self.ds[key]

    def startsWith(self, prefix: str) -> bool:
        key = prefix[0]
        if key not in self.ds:
            return False

        for word in self.ds[key]:
            if word.startswith(prefix):
                return True
        return False


def main():
    word = 'apple'
    obj = Trie()
    obj.insert(word)
    obj.search(word)


if __name__ == '__main__':
	main()