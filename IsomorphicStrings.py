class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dictt = {}
        sett = set()

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in dictt:
                if t[i] not in sett:
                    dictt[s[i]] = t[i]
                    sett.add(t[i])
                else:
                    return False
            else:
                if dictt[s[i]] != t[i]:
                    return False
        
        return True
