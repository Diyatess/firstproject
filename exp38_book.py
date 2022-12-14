class Publisher:
    def __init__(self, name):
        self.name = name


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author


class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def show(self):
        print("Publisher:", self.name)
        print("Book name:", self.title)
        print("Author name:", self.author)
        print("Price:", self.price)
        print("Number of pages:", self.pages)


python_book = Python("O'Reilly Media", "Learning Python", "Mark Lutz", 25.99, 544)
python_book.show()