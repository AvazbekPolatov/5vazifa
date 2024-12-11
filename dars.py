from collections import namedtuple

# users=[
#     (1,'Avazbek', 'Poltov', 20),
#     (2,'Asilbek', 'Omonov', 20),
    
# ]

# Person=namedtuple('Person', ['id', 'first_name', 'last_name', 'age'])


# for user in users:
#     person=Person(*user)
#     print(f"id: {person.id}, ism: {person.first_name}, familiya: {person.last_name}, yosh: {person.age}")

# --------------------------------------------------------------------------------------------------------------  

users=[
    {'id': 1, 'first_name': 'Avazbek', 'last_name': 'Poltov', 'age': 20},
    {'id': 2, 'first_name': 'Asilbek', 'last_name': 'Omonov', 'age': 20},
]

Person=namedtuple('Person', ['id', 'first_name', 'last_name', 'age'])

for user in users:
    person=Person(**user)
    print(f"id: {person.id}, ism: {person.first_name}, familiya: {person.last_name}, yosh: {person.age}")
    
    

# Sequence types

# list
# tuple
# range 

# Closurse types

# set
# frozenset
# dict

