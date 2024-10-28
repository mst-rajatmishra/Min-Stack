class MinStack:
    def __init__(self):
        self.main_stack = []  # Main stack to hold the elements
        self.min_stack = []   # Stack to hold the minimum values

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        # Push onto min stack if it is empty or the new value is <= current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.main_stack:
            top_value = self.main_stack.pop()
            # If the popped value is the current minimum, pop it from the min stack as well
            if top_value == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1] if self.main_stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

# Example usage:
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())  # Output: -3
# minStack.pop()
# print(minStack.top())      # Output: 0
# print(minStack.getMin())   # Output: -2

