# monotonic stack

class StockSpanner(object):

    def __init__(self):
        self.stack = []


    def next(self, price):
        span = 1

        while self.stack and price >= self.stack[-1][0]:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, span])

        return self.stack[-1][1]