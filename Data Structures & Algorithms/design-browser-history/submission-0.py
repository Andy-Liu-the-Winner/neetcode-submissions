class BrowserHistory:

    def __init__(self, homepage: str):
        self.length = 1
        self.p = 0
        self.l = [homepage]

    def visit(self, url: str) -> None:
        self.p += 1
        if self.length == self.p:
            self.l.append(url)
            self.length += 1
        else:
            self.l[self.p] = url
            self.length = self.p + 1

    def back(self, steps: int) -> str:
        if steps > self.p:
            self.p = 0
            return self.l[self.p]
        self.p -= steps
        return self.l[self.p]
        
        

    def forward(self, steps: int) -> str:
        if self.p + steps >= self.length:
            self.p = self.length - 1
            return self.l[self.p]
        self.p += steps
        return self.l[self.p]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)