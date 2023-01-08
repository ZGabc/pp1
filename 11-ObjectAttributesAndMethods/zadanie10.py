class Cell:
    def __init__(self, operator, producent,owner):
        self.operator=operator
        self.producent=producent
        self.owner=owner
    def __str__(self):
        return(f"This is {self.owner}'s phone")
    def state(self):
        pass
    def action(self):
        pass

c1=Cell("orange","Nokia","Matylda")
print(c1)