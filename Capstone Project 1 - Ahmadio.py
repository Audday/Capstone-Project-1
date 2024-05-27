import datetime


books = [
    {'BookID': 1, 'Judul': 'The Little Prince', 'Author': 'Antoine de Saint-Exupéry', 'TahunTerbit' : '06/04/1943', 'category' : 'Anak-Anak', 'available': True},
    {'BookID': 2, 'Judul': 'Harry Potter and the Sorcerer\'s Stone', 'Author': 'J.K. Rowling', 'TahunTerbit' : '26/06/1997', 'category' : 'Fantasi', 'available': True},
    {'BookID': 3, 'Judul': 'To Kill a Mockingbird', 'Author': 'Harper Lee', 'TahunTerbit' : '11/07/1960', 'category' : 'Fiksi', 'available': True},
    {'BookID': 4, 'Judul': '1984', 'Author': 'George Orwell', 'TahunTerbit' : '08/06/1949', 'category' : 'Dystopia', 'available': True},
    {'BookID': 5, 'Judul': 'Pride and Prejudice', 'Author': 'Jane Austen', 'TahunTerbit' : '28/01/1813', 'category' : 'Romansa', 'available': True},
    {'BookID': 6, 'Judul': 'The Great Gatsby', 'Author': 'F. Scott Fitzgerald', 'TahunTerbit' : '10/04/1925', 'category' : 'Fiksi', 'available': True},
    {'BookID': 7, 'Judul': 'Moby-Dick', 'Author': 'Herman Melville', 'TahunTerbit' : '18/10/1851', 'category' : 'Petualangan', 'available': True},
    {'BookID': 8, 'Judul': 'War and Peace', 'Author': 'Leo Tolstoy', 'TahunTerbit' : '01/01/1869', 'category' : 'Sejarah', 'available': True},
    {'BookID': 9, 'Judul': 'The Catcher in the Rye', 'Author': 'J.D. Salinger', 'TahunTerbit' : '16/07/1951', 'category' : 'Fiksi', 'available': True},
    {'BookID': 10, 'Judul': 'The Hobbit', 'Author': 'J.R.R. Tolkien', 'TahunTerbit' : '21/09/1937', 'category' : 'Fantasi', 'available': True},
    {'BookID': 11, 'Judul': 'Ulysses', 'Author': 'James Joyce', 'TahunTerbit' : '02/02/1922', 'category' : 'Modernisme', 'available': True},
    {'BookID': 12, 'Judul': 'The Odyssey', 'Author': 'Homer', 'TahunTerbit' : '01/01/800', 'category' : 'Epik', 'available': True},
    {'BookID': 13, 'Judul': 'Crime and Punishment', 'Author': 'Fyodor Dostoevsky', 'TahunTerbit' : '01/01/1866', 'category' : 'Kriminal', 'available': True},
    {'BookID': 14, 'Judul': 'The Divine Comedy', 'Author': 'Dante Alighieri', 'TahunTerbit' : '01/01/1320', 'category' : 'Puisi', 'available': True},
    {'BookID': 15, 'Judul': 'Brave New World', 'Author': 'Aldous Huxley', 'TahunTerbit' : '01/01/1932', 'category' : 'Dystopia', 'available': True},
    {'BookID': 16, 'Judul': 'Anna Karenina', 'Author': 'Leo Tolstoy', 'TahunTerbit' : '01/01/1877', 'category' : 'Romansa', 'available': True},
    {'BookID': 17, 'Judul': 'The Lord of the Rings', 'Author': 'J.R.R. Tolkien', 'TahunTerbit' : '29/07/1954', 'category' : 'Fantasi', 'available': True},
    {'BookID': 18, 'Judul': 'One Hundred Years of Solitude', 'Author': 'Gabriel Garcia Marquez', 'TahunTerbit' : '05/06/1967', 'category' : 'Fiksi', 'available': True},
    {'BookID': 19, 'Judul': 'Don Quixote', 'Author': 'Miguel de Cervantes', 'TahunTerbit' : '01/01/1605', 'category' : 'Petualangan', 'available': True},
    {'BookID': 20, 'Judul': 'The Brothers Karamazov', 'Author': 'Fyodor Dostoevsky', 'TahunTerbit' : '01/01/1880', 'category' : 'Filosofi', 'available': False},
    {'BookID': 21, 'Judul': 'The Picture of Dorian Gray', 'Author': 'Oscar Wilde', 'TahunTerbit' : '20/06/1890', 'category' : 'Fiksi', 'available': True},
    {'BookID': 22, 'Judul': 'Frankenstein', 'Author': 'Mary Shelley', 'TahunTerbit' : '01/01/1818', 'category' : 'Horor', 'available': True},
    {'BookID': 23, 'Judul': 'Wuthering Heights', 'Author': 'Emily Brontë', 'TahunTerbit' : '01/01/1847', 'category' : 'Romansa', 'available': True},
    {'BookID': 24, 'Judul': 'The Chronicles of Narnia', 'Author': 'C.S. Lewis', 'TahunTerbit' : '16/10/1950', 'category' : 'Fantasi', 'available': True},
    {'BookID': 25, 'Judul': 'Dracula', 'Author': 'Bram Stoker', 'TahunTerbit' : '26/05/1897', 'category' : 'Horor', 'available': True},
    {'BookID': 26, 'Judul': 'The Alchemist', 'Author': 'Paulo Coelho', 'TahunTerbit' : '01/01/1988', 'category' : 'Filsafat', 'available': True},
    {'BookID': 27, 'Judul': 'Les Misérables', 'Author': 'Victor Hugo', 'TahunTerbit' : '01/01/1862', 'category' : 'Sejarah', 'available': True},
    {'BookID': 28, 'Judul': 'The Count of Monte Cristo', 'Author': 'Alexandre Dumas', 'TahunTerbit' : '28/01/1844', 'category' : 'Petualangan', 'available': True},
    {'BookID': 29, 'Judul': 'Alice\'s Adventures in Wonderland', 'Author': 'Lewis Carroll', 'TahunTerbit' : '26/11/1865', 'category' : 'Anak-Anak', 'available': True},
    {'BookID': 30, 'Judul': 'The Secret Garden', 'Author': 'Frances Hodgson Burnett', 'TahunTerbit' : '01/01/1911', 'category' : 'Anak-Anak', 'available': True},
    {'BookID': 31, 'Judul': 'The Adventures of Sherlock Holmes', 'Author': 'Arthur Conan Doyle', 'TahunTerbit' : '14/10/1892', 'category' : 'Detektif', 'available': True},
    {'BookID': 32, 'Judul': 'Gulliver\'s Travels', 'Author': 'Jonathan Swift', 'TahunTerbit' : '28/10/1726', 'category' : 'Petualangan', 'available': True},
    {'BookID': 33, 'Judul': 'The Road', 'Author': 'Cormac McCarthy', 'TahunTerbit' : '26/09/2006', 'category' : 'Post-apokaliptik', 'available': True},
    {'BookID': 34, 'Judul': 'Sapiens: A Brief History of Humankind', 'Author': 'Yuval Noah Harari', 'TahunTerbit' : '01/01/2011', 'category' : 'Sejarah', 'available': True},
    {'BookID': 35, 'Judul': 'The Hunger Games', 'Author': 'Suzanne Collins', 'TahunTerbit' : '14/09/2008', 'category' : 'Distopia', 'available': True},
    {'BookID': 36, 'Judul': 'The Road Not Taken', 'Author': 'Robert Frost', 'TahunTerbit' : '01/01/1916', 'category' : 'Puisi', 'available': True},
    {'BookID': 37, 'Judul': 'Fahrenheit 451', 'Author': 'Ray Bradbury', 'TahunTerbit' : '01/01/1953', 'category' : 'Distopia', 'available': True},
    {'BookID': 38, 'Judul': 'The Name of the Wind', 'Author': 'Patrick Rothfuss', 'TahunTerbit' : '27/03/2007', 'category' : 'Fantasi', 'available': True},
    {'BookID': 39, 'Judul': 'The Kite Runner', 'Author': 'Khaled Hosseini', 'TahunTerbit' : '29/05/2003', 'category' : 'Fiksi', 'available': True},
    {'BookID': 40, 'Judul': 'The Girl with the Dragon Tattoo', 'Author': 'Stieg Larsson', 'TahunTerbit' : '01/01/2005', 'category' : 'Misteri', 'available': True}
]


members = [
    {'memberID': 1, 'name': 'Alice Smith', 'noTlp': '08119873847', 'email': 'alice.smith@gmail.com', 'Alamat': 'Jl. Sukamaju No. 19'},
    {'memberID': 2, 'name': 'Bob Johnson', 'noTlp': '08119873848', 'email': 'bob.johnson@gmail.com', 'Alamat': 'Jl. Sejahtera No. 45'},
    {'memberID': 3, 'name': 'Charlie Davis', 'noTlp': '08119873849', 'email': 'charlie.davis@gmail.com', 'Alamat': 'Jl. Merdeka No. 11'},
    {'memberID': 4, 'name': 'Dana Lee', 'noTlp': '08119873850', 'email': 'dana.lee@gmail.com', 'Alamat': 'Jl. Bahagia No. 7'},
    {'memberID': 5, 'name': 'Eve Martinez', 'noTlp': '08119873851', 'email': 'eve.martinez@gmail.com', 'Alamat': 'Jl. Mawar No. 20'}
]


borrows = []

#============================================================ Fungsi Tabel =========================================================================================================================================#
#============================================================ Fungsi Tabel =========================================================================================================================================#
#============================================================ Fungsi Tabel =========================================================================================================================================#

#Fungsi Pembuatan Tabel Buku
def print_books(books_to_print, start_index):
    headers = ["ID", "Judul", "Author", "Tahun Terbit", "Category", "Available"]
    head = ["BookID", "Judul", "Author", "TahunTerbit", "category", "available"]
    

    column_widths = [max(len(str(book[head])) for book in books_to_print) for head in head]
    column_widths = [max(len(header), width) for header, width in zip(headers, column_widths)]

    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")
    print("| " + " | ".join([header.ljust(width) for header, width in zip(headers, column_widths)]) + " |")
    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")

    for i in range(start_index, min(start_index+10, len(books_to_print))):
        book = books_to_print[i]
        row = "| " + " | ".join([str(book[head]).ljust(width) for head, width in zip(head, column_widths)]) + " |"
        print(row)
    
    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")

#Fungsi Pembuatan Tabel Member
def print_member(member_to_print, start_index):
    headers = ["ID", "Nama", "No Tlp", "Email", "Alamat"]
    head = ["memberID", "name", "noTlp", "email", "Alamat"]
    

    column_widths = [max(len(str(members[head])) for members in member_to_print) for head in head]
    column_widths = [max(len(header), width) for header, width in zip(headers, column_widths)]

    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")
    print("| " + " | ".join([header.ljust(width) for header, width in zip(headers, column_widths)]) + " |")
    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")

    for i in range(start_index, min(start_index+10, len(member_to_print))):
        members = member_to_print[i]
        row = "| " + " | ".join([str(members[head]).ljust(width) for head, width in zip(head, column_widths)]) + " |"
        print(row)
    
    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")

def print_borrows(borrows_to_print, start_index):
    if not borrows_to_print:
        print("Tidak ada data peminjaman yang tersedia.")
        return

    headers = ["ID Peminjaman",  "Nama Peminjam", "Judul Buku", "Penerbit", "Tanggal Meminjam", "Tanggal Pengembalian"]
    head = ["BorrowID",  "Nama Peminjam", "Judul Buku", "Author", "Tanggal Meminjam", "Tanggal Pengembalian"]

    column_widths = [max(len(str(borrow[head])) for borrow in borrows_to_print) for head in head]
    column_widths = [max(len(header), width) for header, width in zip(headers, column_widths)]

    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")
    print("| " + " | ".join([header.ljust(width) for header, width in zip(headers, column_widths)]) + " |")
    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")

    for borrow in borrows_to_print:
        row = "| " + " | ".join([str(borrow[head]).ljust(width) for head, width in zip(head, column_widths)]) + " |"
        print(row)
    
    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")
    


#========================================================= FUNGSI SEARCH ======================================================= #
#========================================================= FUNGSI SEARCH ======================================================= #
#========================================================= FUNGSI SEARCH ======================================================= #

#Fungsi Search Buku
def search_books(query):
    found_books = []
    for book in books:
        if str(query) in str(book['BookID']) or \
            query.lower() in book['Judul'].lower() or \
           query.lower() in book['Author'].lower() or \
           query.lower() in book['category'].lower():
            found_books.append(book)
    return found_books

#Fungsi Search Member
def search_member(query):
    found_members = []
    for member in members:
        if str(query) in str(member['memberID']) or \
            query.lower() in member['name'].lower():
            found_members.append(member)
    return found_members

# Alasan menggunakan str pada ID, di karenakan ID bersifat atau berbentuk INT, dan INT itu tidak iterable, jadi harus mengubahkan menjadi STR terlebih dahulu

#================================ MENU BUKU =====================================================================================================================================================#
#================================ MENU BUKU =====================================================================================================================================================#
#================================ MENU BUKU =====================================================================================================================================================#

#Menambah Buku Ke Dalam Data
def create_books():
        start_index = 0
        while True :
            print_books(books, start_index)

            option = input("<< (P) Previous    (N) Next>>   \n\n(T) Tambah Buku \n(Q) Quit:  ").upper()
            if option == 'N':
                    start_index += 10
                    if start_index >= len(books):
                        print("No more results.")
                        start_index -= 10
                    continue
            elif option == 'P':
                start_index -= 10
                if start_index < 0:
                    print("Already at the beginning.")
                    start_index = 0
                continue
            elif option == 'T':
                max_id = max(book['BookID'] for book in books)
                new_id = max_id + 1 if books else 1 #Menambahkan ID Automatic
                title = input("Masukan judul buku: ")
                existing_books = [book for book in books if book['Judul'].lower() == title.lower()]
                if existing_books:
                    print(f"Buku dengan judul '{title}' sudah ada:")
                    print_books(existing_books, 0)
                    confirm = input("Apakah Anda yakin ingin menambahkan buku dengan judul yang sama? (Y/N) ").upper() # Jika Buku Sudah ada
                    if confirm != 'Y':
                        print("Penambahan buku dibatalkan.")
                        continue
                author = input("Masukan author buku: ")
                year = input("Masukan tahun Terbit (DD/MM/YYYY): ")
                category = input("Masukan category buku: ")
                year = datetime.datetime.strptime(year, "%d/%m/%Y").strftime("%d/%m/%Y")
                books.append({'BookID': new_id, 'Judul': title, 'Author': author, 'TahunTerbit' : year, 'category' : category, 'available': True})
                print(f"Book '{title}' added successfully.")
                continue

            elif option == 'Q':
                print("Exiting...")
                break
            else:
                print("Invalid option.")

#Membaca Buku Pada Data
def read_books():
    start_index = 0
    while True:

        print_books(books, start_index)
        
        option = input("<< (P) Previous    (N) Next>>   \n\nS (Search), \nQ (Quit): ").upper()
        
        if option == 'N':
            start_index += 10
            if start_index >= len(books):
                print("No more results.")
                start_index -= 10
            continue
        elif option == 'P':
            start_index -= 10
            if start_index < 0:
                print("Already at the beginning.")
                start_index = 0
            continue
        elif option == 'S':
            query = input("Enter search query: ")
            search_results = search_books(query)
            if search_results:
                print("\nSearch Results:")
                start_index = 0
                print_books(search_results, start_index)
                while True:
                    move_option = input("<< (P) Previous    (N) Next>>    \n\nQ (Quit): ").upper()
                    if move_option == 'N':
                        start_index += 10
                        if start_index >= len(search_results):
                            print("No more results.")
                            break
                        print_books(search_results, start_index)
                    elif move_option == 'P':
                        start_index -= 10
                        if start_index < 0:
                            print("Already at the beginning.")
                            start_index = 0
                            break
                        print_books(search_results, start_index)
                    elif move_option == 'Q':
                        break
                    else:
                        print("Invalid option.")
            else:
                print("No books found matching the query.")
        elif option == 'Q':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

#Mengupdate Buku Yang Ada Di Data
def update_book():
    start_index = 0
    while True:
        print_books(books, start_index)

        option = input("<< (P) Previous    (N) Next>>   \n\n(U) Update \n(S) Search \n(Q) Quit:  ").upper()
        if option == 'N':
            start_index += 10
            if start_index >= len(books):
                print("Sudah Tidak Ada Hasil")
                start_index -= 10
            continue
        elif option == 'P':
            start_index -= 10
            if start_index < 0:
                print("Sudah Di Awal")
                start_index = 0
            continue
        elif option == 'U':
            identifier = input("Masukan ID/Judul/Category Buku Yang Akan Di Update (or Q to quit): ").upper()

            books_to_update = []
            try:
                book_id = int(identifier)
                books_to_update = [book for book in books if book['BookID'] == book_id]
            except ValueError:
                books_to_update = [book for book in books if book['Judul'].upper() == identifier or book['category'].upper() == identifier]

            if not books_to_update:
                print("Judul/Category/ID Buku Tidak Di Temukan")
                continue

            if len(books_to_update) > 1:
                print("Hasil Yang Sama Di Temukan:")
                print_books(books_to_update, 0)
                book_id = int(input("Masukan ID Yang Ingin Di Update: "))
                book_to_update = next((book for book in books_to_update if book['BookID'] == book_id), None)
                if not book_to_update:
                    print("ID Buku Tidak Di Termukan")
                    continue
            else:
                book_to_update = books_to_update[0]

            print(f"Detail Buku:")
            print_books([book_to_update], 0)

            title = input("Masukan judul buku (leave blank to keep current): ")
            author = input("Masukan author buku (leave blank to keep current): ")
            year = input("Masukan tahun Terbit (DD/MM/YYYY) (leave blank to keep current): ")
            category = input("Masukan category buku (leave blank to keep current): ")

            if title:
                book_to_update['Judul'] = title
            if author:
                book_to_update['Author'] = author
            if year:
                try:
                    book_to_update['TahunTerbit'] = datetime.datetime.strptime(year, "%d/%m/%Y").strftime("%d/%m/%Y")
                except ValueError:
                    print("Format Tanggal Tidak Sesuai (DD/MM/YYYY)!")
            if category:
                book_to_update['category'] = category

            print(f"Nuku Dengan {book_to_update['BookID']} Berhasil Di Perbaharui.")
            continue
        elif option == 'S':
            query = input("Enter search query: ")
            search_results = search_books(query)
            if search_results:
                print("\nSearch Results:")
                start_index = 0
                print_books(search_results, start_index)
                while True:
                    move_option = input("<< (P) Previous    (N) Next>>    \n\nQ (Quit): ").upper()
                    if move_option == 'N':
                        start_index += 10
                        if start_index >= len(search_results):
                            print("No more results.")
                            break
                        print_books(search_results, start_index)
                    elif move_option == 'P':
                        start_index -= 10
                        if start_index < 0:
                            print("Already at the beginning.")
                            start_index = 0
                            break
                        print_books(search_results, start_index)
                    elif move_option == 'Q':
                        break
                    else:
                        print("Invalid option.")
        elif option == 'Q':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

#Menghapus Buku Yang Ada Di Data
def delete_book():
    start_index = 0
    while True:
        print_books(books, start_index)

        option = input("<< (P) Previous    (N) Next>>   \n\n(D) Delete \n(Q) Quit:  ").upper()
        if option == 'N':
            start_index += 10
            if start_index >= len(books):
                print("Sudah Tidak Ada Hasil")
                start_index -= 10
            continue
        elif option == 'P':
            start_index -= 10
            if start_index < 0:
                print("Sudah Di Awal")
                start_index = 0
            continue
        elif option == 'D':
            identifier = input("Masukan ID/Judul/Category Buku Yang Akan Di Update (or Q to quit): ").upper()
            if identifier == 'Q':
                print("Exiting...")
                break

            books_to_delete = []
            try:
                book_id = int(identifier)
                books_to_delete = [book for book in books if book['BookID'] == book_id]
            except ValueError:
                books_to_delete = [book for book in books if book['Judul'].upper() == identifier or book['category'].upper() == identifier]

            if not books_to_delete:
                print("Book with the specified BookID, Judul, or category not found.")
                continue

            if len(books_to_delete) > 1:
                print("Hasil Yang Sama Di Temukan:")
                print_books(books_to_delete, 0)
                book_id = int(input("Enter the BookID of the book you want to delete from the list: "))
                book_to_delete = next((book for book in books_to_delete if book['BookID'] == book_id), None)
                if not book_to_delete:
                    print("Judul/Category/ID Buku Tidak Di Temukan.")
                    continue
            else:
                book_to_delete = books_to_delete[0]

            print(f"Detail Buku Saat Ini (BookID: {book_to_delete['BookID']}):")
            print_books([book_to_delete], 0)

            confirm = input(f"Apakah anda yakin ingin menghapus {book_to_delete['Judul']}? (Y/N): ").upper()
            if confirm == 'Y':
                books.remove(book_to_delete)
                for book in books:
                    if book['BookID'] > book_to_delete['BookID']:
                        book['BookID'] -= 1
                print(f"Book with BookID {book_to_delete['BookID']} has been deleted successfully.")
                continue
            else:
                print("Book deletion canceled.")
            break
        elif option == 'Q':
            print("Exiting...")
            break
        else:
            print("Invalid option.")


def book_menu():
    while True:
        print("\n" + "="*30)
        print("          BOOK MENU")
        print("="*30)
        print("1. Create New Books")
        print("\n2. Show Books")
        print("\n3. Update Books")
        print("\n4. Delete Books")
        print("\n5. Return to Main Menu")
        print("="*30)
        
        choice = input("Masukan Pilihan : ")

        if choice == '1':
            create_books()
        elif choice == '2':
            read_books()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid option.")

#==================================================== MEMBER MENUS =========================================================#
#==================================================== MEMBER MENUS =========================================================#
#==================================================== MEMBER MENUS =========================================================#

def create_member():
        start_index = 0
        while True:
            print_member(members, start_index)
            option = input("<< (P) Previous    (N) Next>>   \n\n(T) Tambah Member \n(Q) Quit:  ").upper()
            if option == 'N':
                start_index += 10
                if start_index >= len(members):
                    print("No more results.")
                    start_index -= 10
                continue
            elif option == 'P':
                start_index -= 10
                if start_index < 0:
                    print("Already at the beginning.")
                    start_index = 0
                continue
            elif option == 'T':
                    max_id = max(member['memberID'] for member in members)
                    new_id = max_id + 1 if members else 1
                    name = input("Masukan nama member: ")
                    existing_members = [member for member in members if member['name'].lower() == name.lower()]
                    if existing_members:
                        print(f"Member dengan nama '{name}' sudah ada:")
                        print_member(existing_members, 0)
                        confirm = input("Apakah Anda yakin ingin menambahkan member dengan nama yang sama? (Y/N) ").upper()
                        if confirm != 'Y':
                            print("Penambahan member dibatalkan.")
                            continue
                    noTlp = input("Masukan nomor telepon: ")
                    email = input("Masukan email: ")
                    Alamat = input("Masukan alamat: ")
                    members.append({'memberID': new_id, 'name': name, 'noTlp': noTlp, 'email' : email, 'Alamat' : Alamat})
                    print(f"Member '{name}' added successfully.")
                    continue
            elif option == 'Q':
                print("Exiting...")
                return
            else:
                print("Invalid option.")

def read_member():
    start_index = 0
    while True:
        print_member(members, start_index)
        
        option = input("<< (P) Previous    (N) Next>>   \n\nS (Search), \nQ (Quit): ").upper()
        
        if option == 'N':
            start_index += 10
            if start_index >= len(members):
                print("No more results.")
                start_index -= 10
            continue
        elif option == 'P':
            start_index -= 10
            if start_index < 0:
                print("Already at the beginning.")
                start_index = 0
            continue
        elif option == 'S':
            query = input("Search :  ")
            search_results = search_member(query)
            if search_results:
                print("\nSearch Results:")
                start_index = 0
                print_member(search_results, start_index)
                while True:
                    move_option = input("<< (P) Previous    (N) Next>>    Q (Quit): ").upper()
                    if move_option == 'N':
                        start_index += 10
                        if start_index >= len(search_results):
                            print("No more results.")
                            break
                        print_member(search_results, start_index)
                    elif move_option == 'P':
                        start_index -= 10
                        if start_index < 0:
                            print("Already at the beginning.")
                            start_index = 0
                            break
                        print_member(search_results, start_index)
                    elif move_option == 'Q':
                        break
                    else:
                        print("Invalid option.")
            else:
                print("No members found matching the query.")
        elif option == 'Q':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

def update_member():
    start_index = 0
    while True:
        print_member(members, start_index)

        option = input("<< (P) Previous    (N) Next>>   \n\n(U) Update \n(Q) Quit:  ").upper()
        if option == 'N':
            start_index += 10
            if start_index >= len(members):
                print("No More Result.")
                start_index -= 10
            continue
        elif option == 'P':
            start_index -= 10
            if start_index < 0:
                print("Already at the beginning")
                start_index = 0
            continue
        elif option == 'U':
            identifier = input("Masukan ID/Nama/Email Member Yang Akan Di Update (or Q to quit): ").upper()

            members_to_update = []
            try:
                member_id = int(identifier)
                members_to_update = [member for member in members if member['memberID'] == member_id]
            except ValueError:
                members_to_update = [member for member in members if member['name'].upper() == identifier or member['email'].upper() == identifier]

            if not members_to_update:
                print("Member dengan ID/Nama/Email yang diidentifikasi tidak ditemukan")
                continue

            if len(members_to_update) > 1:
                print("Hasil yang sama ditemukan:")
                print_member(members_to_update, 0)
                member_id = int(input("Masukkan MemberID dari member yang ingin diperbarui: "))
                member_to_update = next((member for member in members_to_update if member['memberID'] == member_id), None)
                if not member_to_update:
                    print("Member dengan ID yang ditentukan tidak ditemukan")
                    continue
            else:
                member_to_update = members_to_update[0]

            print(f"Detail Member:")
            print_member([member_to_update], 0)

            nama = input("Masukkan nama member (biarkan kosong untuk mempertahankan yang sekarang): ")
            noTlp = input("Masukkan noTlp member (biarkan kosong untuk mempertahankan yang sekarang): ")
            email = input("Masukkan email member (biarkan kosong untuk mempertahankan yang sekarang): ")

            if nama:
                member_to_update['name'] = nama
            if noTlp:
                member_to_update['noTlp'] = noTlp
            if email:
                member_to_update['email'] = email

            print(f"Member {member_to_update['name']} berhasil diperbarui.")
            continue

        elif option == 'Q':
            print("Exiting...")
            break
        else:
            print("Invalid Option.")

def delete_member():
    start_index = 0
    while True:
        print_member(members, start_index)

        option = input("<< (P) Previous    (N) Next>>   \n\n(D) Delete \n(Q) Quit:  ").upper()
        if option == 'N':
            start_index += 10
            if start_index >= len(members):
                print("Sudah Tidak Ada Hasil")
                start_index -= 10
            continue
        elif option == 'P':
            start_index -= 10
            if start_index < 0:
                print("Sudah Di Awal")
                start_index = 0
            continue
        elif option == 'D':
            identifier = input("Masukan ID/Nama/Email Member Yang Akan Di Hapus (atau Q untuk keluar): ").upper()
            if identifier == 'Q':
                print("Exiting...")
                break

            members_to_delete = []
            try:
                member_id = int(identifier)
                members_to_delete = [member for member in members if member['memberID'] == member_id]
            except ValueError:
                members_to_delete = [member for member in members if member['name'].upper() == identifier or member['email'].upper() == identifier]

            if not members_to_delete:
                print("Member dengan ID/Nama/Email yang diidentifikasi tidak ditemukan.")
                continue

            if len(members_to_delete) > 1:
                print("Banyak hasil yang ditemukan:")
                print_member(members_to_delete, 0)
                member_id = int(input("Masukkan MemberID dari member yang ingin dihapus dari daftar: "))
                member_to_delete = next((member for member in members_to_delete if member['MemberID'] == member_id), None)
                if not member_to_delete:
                    print("Member dengan ID yang ditentukan tidak ditemukan.")
                    continue
            else:
                member_to_delete = members_to_delete[0]

            print(f"Detail Member saat ini (MemberID: {member_to_delete['memberID']}):")
            print_member([member_to_delete], 0)

            confirm = input(f"Apakah Anda yakin ingin menghapus {member_to_delete['name']}? (Y/N): ").upper()
            if confirm == 'Y':
                members.remove(member_to_delete)
                for member in members:
                    if member['memberID'] > member_to_delete['memberID']:
                        member['memberID'] -= 1
                print(f"Member dengan MemberID {member_to_delete['name']} berhasil dihapus.")
                continue
            else:
                print("Penghapusan member dibatalkan.")
            break
        elif option == 'Q':
            print("Exiting...")
            break
        else:
            print("Opsi tidak valid.")

def member_menu():
    while True:
        print("\n" + "="*30)
        print("          MEMBER MENU")
        print("="*30)
        print("1. Create New Member")
        print("\n2. Show Member")
        print("\n3. Update Member")
        print("\n4. Delete Member")
        print("\n5. Return to Main Menu")
        print("="*30)
        
        choice = input("Enter your choice: ")

        if choice == '1':
            create_member()
        elif choice == '2':
            read_member()
        elif choice == '3':
            update_member()
        elif choice == '4':
            delete_member()
        elif choice == '5':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid option.")

#=================================================== Peminjaman Buku ==================================================#
#=================================================== Peminjaman Buku ==================================================#
#=================================================== Peminjaman Buku ==================================================#

def borrow_book():
    print("Peminjaman Buku")
    print_member(members, 0)
    member_id = input("Masukkan ID Anggota: ")

    member = next((m for m in members if str(m['memberID']) == member_id), None)
    if not member:
        print("ID Anggota tidak valid.")
        return

    start_index = 0
    while True:
        print_books(books, start_index)
        
        while True:
            option = input("Masukkan Judul Buku yang Ingin Dipinjam (Q untuk keluar), (P) Previous, (N) Next: ").upper()
            if option == 'Q':
                return
            elif option == 'P':
                start_index -= 10
                if start_index < 0:
                    print("Sudah Di Awal")
                    start_index = 0
                break
            elif option == 'N':
                start_index += 10
                if start_index >= len(books):
                    print("Sudah Tidak Ada Hasil")
                    start_index -= 10
                break
            else:
                book = next((b for b in books if b['Judul'].lower() == option.lower()), None)
                if not book:
                    print("Judul buku tidak valid.")
                    continue

                if not book['available']:
                    print("Buku tidak tersedia untuk dipinjam.")
                    continue

                borrow_id = len(borrows) + 1
                borrow_date = datetime.datetime.now().strftime("%d/%m/%Y")
                return_date = None

                borrows.append({
                    'BorrowID': borrow_id,
                    'memberID': member_id,
                    'Nama Peminjam': member['name'],
                    'Judul Buku': book['Judul'],
                    'Author': book['Author'],
                    'Tanggal Meminjam': borrow_date,
                    'Tanggal Pengembalian': return_date
                })

                book['available'] = False
                print("Buku berhasil dipinjam.")
                break
        
        if option == 'Q':
            break

def return_book():
    print_borrows(borrows, 0)
    while True:
        borrow_id = input("Masukkan ID Peminjaman: ")
        borrow = next((b for b in borrows if str(b['BorrowID']) == borrow_id), None)
        if not borrow:
            print("ID Peminjaman tidak valid.")
            return
        
        # Tanggal pengembalian diisi dengan tanggal saat ini
        borrow['Tanggal Pengembalian'] = datetime.datetime.now().strftime("%d/%m/%Y")
        
        book = next((b for b in books if b['Judul'] == borrow['Judul Buku']), None)
        if book:
            book['available'] = True
        else:
            print("Buku tidak ditemukan.")
            return
        
        print("Buku berhasil dikembalikan.")
        break



def borrow_menu():
    while True:
        print("\n" + "="*30)
        print("   PEMINJAMAN BUKU")
        print("="*30)
        print("1. Membuat Pinjaman Baru")
        print("\n2. Show Peminjam")
        print("\n3. Kembalikan Buku")
        print("\n4. Return to Main Menu")
        print("="*30)
        
        choice = input("Enter your choice: ")

        if choice == '1':
            borrow_book()
        elif choice == '2':
            print_borrows(borrows, 0)
        elif choice == '3':
            return_book()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("The option you've entered is not valid.")
#=================================================== Main Menu ==================================================#
#=================================================== Main Menu ==================================================#
#=================================================== Main Menu ==================================================#

#Main Menu Untuk Memilih Opsi
def main_menu():
    while True:
        print("\n" + "="*30)
        print("   Library Management System")
        print("="*30)
        print("1. Book Menu")
        print("\n2. Member Menu")
        print("\n3. Borrowing Menu")
        print("\n4. Return to Main Menu")
        print("="*30)
        
        choice = input("Enter your choice: ")

        if choice == '1':
            book_menu()
        elif choice == '2':
            member_menu()
        elif choice == '3':
            borrow_menu()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("The option you've entered is not valid.")

# Run the main menu
main_menu()