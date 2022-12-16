class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dictt = {"b": 0, "a": 0, "l":0, "o":0, "n":0}
        count = 0
        for i in text:
            if i in dictt:
                dictt[i] +=1
        
        if dictt["l"] < 2 or dictt["o"] <2:
            return count
        
        while True:
            for i in dictt:
                if dictt[i] <= 0:
                    return count
                if i == "l" or i =="o":
                    dictt[i] -=2
                    if dictt[i] < 0:
                        return count
                else:
                    dictt[i] -=1

            count +=1
