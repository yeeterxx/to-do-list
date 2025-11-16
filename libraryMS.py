class Books:
    def __init__(self,title,author):
        self.title= title
        self.author= author 
        self.available=True

    def borrow(self):
        if self.available==True:
            self.available=False
            print("book borrowed !!")
        else:
            print("book not available to borrow!!")

    def return_book(self):
        if self.available==False:
            self.available=True
            print("book returned sucessfully!!")
        else:
            print("book already available!!")


books=[
    Books("harry potter","jk rowling"),
    Books("one piece","eichiro oda"),
    Books("History of time", "stephen hawking")
]

def view_all():
    for index,book in enumerate(books):
        status= "available " if book.available else "unavailable"
        print(f'{index}. {book.title}:{book.author} - {status} ')


while True:

        print("\n-- Library Management --")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Quit")
        
        try:
            choice=int(input("enter a choice :"))
        except:
            print("value error!!")
            continue

        if choice==1:
            view_all()

        elif choice==2:
            view_all()
            try:
             pick= int(input("pick book to borrow:"))
             books[pick].borrow()
            except:
                print("invalid request!!")
                continue

        elif choice==3:
            view_all()
            try:
                pick=int(input("enter the book to return"))
                books[pick].return_book()
            except:
                print("invalid request")
                continue

        elif choice==4:
            break



    
    
    




        