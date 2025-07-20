import json

filename = "library.json"

#view all books

def option_1():
    print("You have selected to view all books.")
    
    with open(filename, "r") as file:
        data = json.load(file)
        books = data.get("books", [])
    if not books:
        print("Library is empty")
    else:
        for i, book in enumerate(books):
            print(f"{i}: Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")


#add new books

def option_2():
    print("You have selected to add new books.")
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication: ")
    genre = input("Enter the genre of the book: ")

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    }

    with open (filename, "r") as file:
        data = json.load(file)
        data["books"].append(new_book)

    with open (filename, "w") as file:
        json.dump(data, file, indent=4)
    print("Just added:", new_book)

    
    
#main menu

def main_menu():
    print("Welcome to the library! What would you like to do?")
    print("1. View all books")
    print("2. Add new books")
    print("3. Exit")

    while True: 
        choice = input("Enter you choice (1-3): ")
        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            print("You have selected to exit.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()


