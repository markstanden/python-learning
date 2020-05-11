#from sys import argv
#import io

def initialise_book():
    book = {}
    book = add_record(book, "Ref Name", "Real Name", "Email address", "Phone Number")
    return book

def add_record (book, ref_name, name, email, number):
    new_record =    { "name" : name,
                    "email" : email,
                    "number" : number }
    book = {ref_name : new_record}
    return book

#if FileNotFoundError(argv[1]):
#    print("Error: Saved address book not found")
#    saved_add_book = io.__file__
#else:
#    print("Success: Saved address book found")
#    saved_add_book = open(argv[1])

address_book = initialise_book()
print(address_book)
address_book.pop("Ref Name")
print(address_book)