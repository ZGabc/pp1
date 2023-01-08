class Book:
    def __init__(self, title, author,lengh ):
        self.title = title
        self.author = author
        self.lengh = lengh
    def __str__(self):
        return f"{self.title}, {self.author}, {self.lengh} pages"
    

book1= Book("Alice in Wonderland","Lewis Carroll", 192)

print(book1)