name=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

count=len(name[0])
for i in range(len(name)):
    if count<len(name[i-1]):
        count=len(name[i-1])
        long=name[i-1]
print(long)