from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for r in ransomNote:
            if not counter[r]: 
                return False
            elif counter[r] > 0: 
                counter[r] -= 1
  
        return True
        