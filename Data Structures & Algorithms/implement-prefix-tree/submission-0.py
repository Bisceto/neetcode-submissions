class PrefixTree:
    #Hashmap. key = char, value = hashmap of it's children
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['#'] = True


    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char in cur:
                cur = cur[char]
            else:
                return False
        if '#' in cur: 
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char in cur:
                cur = cur[char]
            else:
                return False
        if len(cur) > 0:
            return True
        else:
            return False
        
        