# دیکشنری حیوانات
pet1 = {'name': 'buddy', 'type': 'dog', 'owner': 'alice'}
pet2 = {'name': 'whiskers', 'type': 'cat', 'owner': 'bob'}
pet3 = {'name': 'nemo', 'type': 'fish', 'owner': 'carol'}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"\nName: {pet['name'].title()}")
    print(f"Type: {pet['type'].title()}")
    print(f"Owner: {pet['owner'].title()}")
