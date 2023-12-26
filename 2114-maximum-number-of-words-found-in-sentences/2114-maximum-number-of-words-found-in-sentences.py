class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        count = 0
        for i in sentences:
            words = list()
            words = i.split(" ")
            mx = max(len(words),count)
            count = mx
            
        return count