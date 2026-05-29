class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_a = {}
        temp_b = {}
        for c in s:
            if c not in temp_a:
                temp_a[c]=0
            temp_a[c]+=1
        
        for char in t:
            if char not in temp_b:
                temp_b[char]=0
            temp_b[char]+=1

        
        if temp_a == temp_b:
            return True
        else:
            return False

