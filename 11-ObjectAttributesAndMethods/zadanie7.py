class Student:
    uni="UEK Kraków"
    id=10000

    def __init__(self,name, surname, std):
        self.name=name
        self.surname=surname
        self.std=std
        self.id=Student.id
        Student.id+=1

    def __str__(self):
        return(f"{self.name} {self.surname} ({Student.id}), {self.std}, {Student.uni} ")

    

s1=Student("Zofia","Ostrowska","Applied Informatics" )
print(s1)
s2=Student("Anna","Maj", "Informatyka")

print(s2)
