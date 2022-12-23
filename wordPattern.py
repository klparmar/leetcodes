class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictt = {}
        curr = 0
        taken = {}
        words = s.split()
        for i in words:
            if pattern[curr] not in dictt:
                if i not in taken:
                    dictt[pattern[curr]] = i
                    taken[i] = pattern[curr]
                elif taken[i] != pattern[curr]:
                    return False
            else:
                if dictt[pattern[curr]] != i:
                    return False
            curr +=1
            if curr >= len(pattern):
                    break

        if len(pattern) != len(words):
            return False

        return True
