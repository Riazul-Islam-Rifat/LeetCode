# Time complexity O(1)
class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # The next part keeps track of the minimum value
        if len(self.minStack)==0:
            self.minStack.append(val) # When there is no value in stack the current value is the minimum value
        else: # Otherwise we compare with the last value of the stack.
            if val <= self.minStack[-1]:
                self.minStack.append(val)
            else: # If the current value is not the minimum one then we append the last value of the stack again.
                self.minStack.append(self.minStack[-1])
    def pop(self) -> None:
        # When we pop a value we also pop it's corresponding minimum value
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()