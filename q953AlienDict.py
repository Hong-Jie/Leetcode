class Solution:    
    dictAllen={}
    
    def isBigger(self, wordA, wordB):     
        for index in range(min(len(wordA), len(wordB))):
            a = wordA[index]
            b = wordB[index]
            if self.dictAllen[a] < self.dictAllen[b]:
                return False
            elif self.dictAllen[a] > self.dictAllen[b]:
                return True
        return len(wordA)>len(wordB)
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for val, ch in enumerate(order):
            self.dictAllen[ch] = val+1
            
        for index in range(len(words)-1):
            if self.isBigger(words[index], words[index+1]):
                return False
        return True
