class Song:
    def __init__(self,title,performer, album, year):
        self.title=title
        self.performer=performer
        self.album=album
        self.year=year

    def __str__(self):
        return f"""Song:{self.title}
Performer: {self.performer}
Album: {self.album}
Year: {self.year}"""

s1=Song("Killer Queen", "Queen", "Sheer heart attack", 1974)
s2=Song("rgewg","sgewrg","grwgq4",1234)
s3=Song("inna piosenka","inny autor","inny album",1234)
print(s1)
print(s2)