class FunctionStack:
    def __init__(self):
        self.stack = []
        self.executed_functions = set()

    def add(self, func):
        if func not in self.executed_functions:
            self.stack.append(func)
            self.executed_functions.add(func)

    def run(self):
        while self.stack:
            func = self.stack.pop()
            func()
