class library:
    def __init__(self):
        self.__books = []

    def add_books(self,title,author,sl_no,quantity):
        self.title = title
        self.author = author
        self.sl_no = sl_no
        self.__quantity = quantity if quantity>0 else (_ for _ in ()).throw(Exception("quantity cannot be -ve"))
        new_book = [self.title,self.author,self.sl_no,self.__quantity]
        self.__books.append(new_book)

    def show_books(self):
        for i in range(len(self.__books)):
            print(f"Book {i+1}.Title :{self.__books[i][0]} | Author :{self.__books[i][1] } | sl_no :{self.__books[i][2]} | Quantity :{self.__books[i][3]}")

    def borrow_books(self,title,author,sl_no,quantity):
        for index,book in enumerate(self.__books):

            if book[0]==title and book[1]==author and book[2] == sl_no:

                if quantity > book[3]:
                    print("not enough books")
                else:
                    self.__books[index][3] -= quantity
                    if self.__books[index][3]==0:
                        self.__books.remove(book)
                return
            
        print("book doesent exist")

    def return_books(self,title,author,sl_no,quantity):
        if quantity <= 0:
            print(f"quantity cannot be {quantity}")
            return 
        for index,book in enumerate(self.__books):
            if book[0]==title and book[1]==author and book[2] == sl_no:
                self.__books[index][3] += quantity
                return
        self.__books.append([title,author,sl_no,quantity])
        print(f"new book added title : {title} and quantity : {quantity}")

    def search_book(self,title,author,sl_no):
        for index,book in enumerate(self.__books):
            if book[0]==title and book[1]==author and book[2] == sl_no:
                print("book exist")
                return
        print("book doesen't exist")

class entry(library):
    def user_login(self):
        self.uid = input("enter your uid :")
    def login(self):
        with open("darkblade_uids.txt",'r') as f:
            uid_list=[text.strip() for text in f]
        if self.uid not in uid_list:
            return False
        return True
    def user_objective(self):
        print("enter\n\'1\' for showing available books\n\'2\' for adding a book\n\'3\' for borrowing a book\n\'4\' for returning a book\n\'5\' for searching a book")
        self.purpose = int(input("enter your purpose :"))
    def user_exit(self):
        self.exit_var = input("enter \'yes\' if you want to exit otherwise enter \'no\' :")
person = entry()
person.user_login()
log=person.login()

while True:
    if log:
        person.user_objective()
        if person.purpose == 1:
            person.show_books()
        elif person.purpose == 2:
            t = input("Title: ")
            a = input("Author: ")
            s = input("Serial No: ")
            q = int(input("Quantity: "))
            person.add_books(t,a,s,q)
        elif person.purpose == 3:
            t = input("Title: ")
            a = input("Author: ")
            s = input("Serial No: ")
            q = int(input("Quantity to borrow: "))
            person.borrow_books(t, a, s, q)
        elif person.purpose == 4:
            t = input("Title: ")
            a = input("Author: ")
            s = input("Serial No: ")
            q = int(input("Quantity to return: "))
            person.return_books(t, a, s, q)
        elif person.purpose == 5:
            t = input("Title: ")
            a = input("Author: ")
            s = input("Serial No: ")
            person.search_book(t, a, s)
        else:
            print("invalid choice")
        person.user_exit()
        if person.exit_var == "yes":
            break
    else :
        print("your uid is not in our data base please enter a valid data base")
        break

            
        
        
