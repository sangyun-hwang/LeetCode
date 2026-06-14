class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        p_to_w = {}
        w_to_p = {}

        for p, word in zip(pattern, words):
            if p in p_to_w and p_to_w[p] != word:
                return False
            if word in w_to_p and w_to_p[word] != p:
                return False
            
            p_to_w[p] = word
            w_to_p[word] = p

        return True