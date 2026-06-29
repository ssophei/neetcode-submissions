class MinStack:

    def __init__(self):
        self.vals = []

    def push(self, val: int) -> None:
        self.vals.append(val)

    def pop(self) -> None:
        self.vals.pop(-1)

    def top(self) -> int:
        return self.vals[-1]        

    def getMin(self) -> int:
        return min(self.vals)
