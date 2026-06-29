class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections

        char_map = collections.defaultdict(int)

        for char in magazine:
            char_map[char] += 1 

        for char in ransomNote:
            char_map[char] -= 1 
            if char_map[char] < 0:
                return False

        return True
        