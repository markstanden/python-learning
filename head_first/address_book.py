from sys import argv
from random import randint
import pickle
import pprint

NEW_BOOK = 'UNDEFINED'

def save_add_book(sent_book, file_name):
    """Uses pickle to save the book in the user directory"""
    
    #'borrowed' from online source, works really well, with/as still a bit of a mystery
    if NEW_BOOK == True:
        
        # and does book already exist
        print('book already exists - overwrite? (must type yes): ')
        over_write = input()
        #print (overwrite)
        
        if over_write == 'yes':
            with open('user/' + file_name + '.pkl', 'wb') as add_book_file:
                pickle.dump(sent_book, add_book_file, pickle.HIGHEST_PROTOCOL)
        else:
                print("I'm not going to overwrite")
    else:
        with open('user/' + file_name + '.pkl', 'wb') as add_book_file:
            pickle.dump(sent_book, add_book_file, pickle.HIGHEST_PROTOCOL)

def load_add_book(file_name):
    """Uses pickle to load the book from the user directory, returns the book"""

    #'borrowed' from online source, works really well, with/as still a bit of a mystery
    with open('user/' + file_name + '.pkl', 'rb') as add_book_file:
        #returns the loaded from file object
        return pickle.load(add_book_file)

def initialise_book():
    """Creates a blank book, (currently adds a template record, for testing) and returns the created book"""
    
    #create an empty dict
    book = {}

    #call the add_record function, with the 
    book = add_record(book, "Ref Name", "Real Name", "Email address", "Phone Number")
    return book

def add_record (book, ref_name, name, email, number):
    """adds a record to the sent book, using the sent arguments, returns the updated book"""

    #Create the new dict with with sent arguments
    new_record =    {"name" : name,
                    "email" : email,
                   "number" : number }

    #checks whether the reference name already exists, if not, create a blank entry
    book.setdefault(ref_name, "")

    ## need to change for proper error handling, once i've got that far!
    if book[ref_name] == "":
        #must have just been created, so add the new record
        book[ref_name] = new_record
    else:
        #already in the book, so create a random number and attach to the reference.
        print("ref_name already exists")
        ref_name = ref_name + str(randint(0, 999))
        book[ref_name] = new_record

    #return the updated book
    return book

address_book = initialise_book()

## The address book code.  
try:
    addbook = argv[1]
    print('Addbook argument :' + addbook)
    address_book = load_add_book(addbook)
    print(f'Loaded address book START: {address_book}')
    NEW_BOOK = False
except:
    pass
else:
    print("No arguments from me")
    print("Creating new book")
    NEW_BOOK = True
    address_book = initialise_book()


# loads the 'addbook' file from disk
#address_book = load_add_book("addbook")

#add a record 
address_book = add_record(address_book, "Hardcoded_entry", "Mark", "Me@Me.com", "01234 567 890")

pprint.pprint(address_book)
save_add_book(address_book, addbook)