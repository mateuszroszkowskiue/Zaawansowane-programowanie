class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)

        return average > 50

    def __str__(self):
        avg = sum(self.marks) / len(self.marks)
        return f"Student: {self.name} (Średnia: {avg:.1f})"

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka: {self.city}, ul. {self.street}, {self.zip_code}\n"
            f"Godziny otwarcia: {self.open_hours}, telefon: {self.phone}"
        )

class Employee:
    def __init__(self, first_name, last_name, hire_date, birh_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.bith_date = birh_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik: {self.first_name} {self.last_name}\n"
            f"Data zatrudnienia: {self.hire_date}\n"
            f"Data urodzenia: {self.bith_date}\n"
            f"Dane zamieszkania: {self.city}, ul. {self.street}, {self.zip_code}\n"
            f"Telefon: {self.phone}"
        )

class Book:
    def __init__(self, title, library, publication_date, author_name, author_surname, number_of_pages):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f'Książka "{self.title}" - {self.author_name} {self.author_surname}\n'
            f"({self.publication_date}), Stron: {self.number_of_pages}\n"
            f"Biblioteka: {self.library}"
        )

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_list = "\n - ".join([str(book) for book in self.books])
        return (
            f"Zamówienie z dnia {self.order_date} \n"
            f"{self.employee}"
            f"Student: {self.student}"
            f"Zamówione książki: \n - {books_list}"
        )

lib1 = Library("Katowice", "Miła 1", "48-492", "Pon-Pt: 08:00 - 20:00", "123456789")
lib2 = Library("Warszawa", "Mazowiecka 2", "01-120", "Pon-Sob: 09:00 - 18:00", "987654321")

book1 = Book("Wiedźmin", lib1, "1993", "Andrzej", "Sapkowski", 320)
book2 = Book("Lalka", lib1, "1890", "Bolesław", "Prus", 500)
book3 = Book("Pan Tadeusz", lib2, "1834", "Adam", "Mickiewicz", 350)
book4 = Book("Hobbit", lib2, "1937", "J.R.R.", "Tolkien", 310)
book5 = Book("Solaris", lib1, "1961", "Stanisław", "Lem", 220)

emp1 = Employee("Jan", "Kowalski", "2020-01-15", "1990-05-12", "Warszawa", "Polna 10", "00-625", "555111222")
emp2 = Employee("Anna", "Nowak", "2021-06-01", "1992-08-20", "Kraków", "Długa 5", "31-147", "555333444")
emp3 = Employee("Piotr", "Zieliński", "2022-03-10", "1988-11-05", "Warszawa", "Szeroka 3", "00-712", "555666777")

stud1 = Student("Katarzyna Wiśniewska", [70, 80, 90])
stud2 = Student("Michał Wójcik", [40, 45, 50])
stud3 = Student("Magdalena Kamińska", [85, 90, 95])

order1 = Order(emp1, stud1, [book1, book2], "2026-10-24")
order2 = Order(emp2, stud2, [book3, book4, book5], "2026-10-30")

print(order1)
print("\n")
print(order2)