dict_person001 = {
    'name' : 'Mark',
    'age' : '40',
    #'programmer' : False
    }

dict_person002 = {
    'name' : 'Mattan',
    'age' : '32',
    'programmer' : True
    }

dict_person003 = {
    'name' : 'Kelly',
    #'age' : '42',
    'programmer' : False
    }

list_people = [
    dict_person001,
    dict_person002,
    dict_person003
    ]

print()
for person in list_people:
    print('Name : \t\t', person.get('name', 'Classified') )
    print('Age : \t\t', person.get('age', 'Classified') )
    print('Programmer : \t', person.get('programmer', 'Classified') )
    print()