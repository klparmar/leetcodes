class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.q2 = self.q1[::-1]

    def pop(self) -> int:
        return self.q2.pop(0)
        self.q1 = self.q2[::-1]


    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return self.q2 == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
