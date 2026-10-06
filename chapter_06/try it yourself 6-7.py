# دیکشنری فرد اول
person1 = {
    'first_name': 'albert',
    'last_name': 'einstein',
    'age': 76,
    'city': 'princeton'
}

# دیکشنری فرد دوم
person2 = {
    'first_name': 'marie',
    'last_name': 'curie',
    'age': 66,
    'city': 'paris'
}

# دیکشنری فرد سوم
person3 = {
    'first_name': 'isaac',
    'last_name': 'newton',
    'age': 84,
    'city': 'cambridge'
}
people = [person1, person2, person3]
for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"\nFull Name: {full_name}")
    print(f"Age: {age}")
    print(f"City: {city}")
