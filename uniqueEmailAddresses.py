class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        str = ""

        dctt = set()
        ignore = False
        inDomain = False

        for i in emails:
            for j in i:
                if inDomain:
                    str +=j
                elif j == "+":
                    ignore = True
                elif j == "@":
                    ignore = False
                    str +=j
                    inDomain = True
                elif j != "." and not ignore:
                    str += j
            if str not in dctt:
                dctt.add(str)
            str = ""
            inDomain = False
            
        return len(dctt)
