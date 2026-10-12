# Python dictionary
# create a person dictionary
person = {
    'firstName':'Paskal',
    'lastName' :'Kebabe',
    'age'      :21,
    'favourite_colors':['blue','green','black'],
    'is_admin':True
}

print(person)

# accessing the first name
print(person["firstName"])
print(person["age"])

# accessing specific color
print(person['favourite_colors'][1])

# changing values in a dictionary
person['age'] = 20
print(person)

person['Gender'] = {'female'}
print(person)

# delete/remove values in a dictionary
person['favourite_colors'].pop(2)
print(person)

del person['age']
print(person)
