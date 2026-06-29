class MinStack:

    def __init__(self):
        self.vals = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.minstack[-1] == self.vals[-1]:
            self.minstack.pop(-1)
        self.vals.pop(-1)

    def top(self) -> int:
        return self.vals[-1]    

    def getMin(self) -> int:
        return self.minstack[-1]
