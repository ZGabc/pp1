class University():

    # object constructor (__init__ method)
    def __init__(self, name, ):
        # object attributes (object features)
        self.name = name    

    # object methods (object behaviors)
    def print_name(self):  
        print(self.name)

    def __str__(self):
        return f"{self.name}"

u1= University("UEK")

print(u1)
