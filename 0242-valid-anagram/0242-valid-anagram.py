class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return count_str(s) == count_str(t)

def count_str(text):
    count = {}

    for ch in text:
        count[ch] = count.get(ch, 0) + 1

    return count

        