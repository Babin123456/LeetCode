class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i
        
        root.best_index = global_best_idx
        
        for idx, word in enumerate(wordsContainer):
            curr = root
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                if curr.best_index == -1:
                    curr.best_index = idx
                else:
                    curr_best_len = len(wordsContainer[curr.best_index])
                    if len(word) < curr_best_len:
                        curr.best_index = idx

        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            ans.append(curr.best_index)
            
        return ans
