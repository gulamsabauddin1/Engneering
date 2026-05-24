"""Given two strings s and t, return true if t is an anagram of s, and false otherwise."""
class Solution (object):
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for letter in s:
            count[letter]=count.get(letter,0)+1    
        for letter in t:
            if count.get(letter, 0) == 0:
                return False
            count[letter] -= 1    
        return True    
    




s="anagram"
t="nagaram"
print(Solution.isAnagram(s,t))        
    

