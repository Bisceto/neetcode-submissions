class WordDictionary:
    # Trie again 
    def __init__(self):
        self.hm = {}

    def addWord(self, word: str) -> None:
        cur = self.hm
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['#'] = True
        

    def search(self, word: str) -> bool:
        def helper(idx, cur):
            if idx == len(word):
                return '#' in cur
            char = word[idx]
            if char != '.':
                if char not in cur:
                    return False
                return helper(idx + 1, cur[char])
            
            else: #Means it is a dot
                for child in cur:
                    if child != '#' and helper(idx + 1, cur[child]):
                        return True
                return False

        return helper(0, self.hm)

        
