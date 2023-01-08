class TV():

    def __init__(self, name, status):
        self.name=name 
        self.status=status

    def __str__(self):
        return f"{self.name} is {self.show_status}"

    def turn_off(self):
        status=0
        return status 

    def turn_on(self):
        status=1
        return status
    

    def show_status(self, status):
        return(f"TV is:{status}")
    
Tv=TV("LG",1)
TV.turn_off
print(TV.show_status)

